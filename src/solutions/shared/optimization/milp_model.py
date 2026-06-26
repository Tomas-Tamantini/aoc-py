from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from math import inf

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


class Sense(StrEnum):
    MINIMIZE = "minimize"
    MAXIMIZE = "maximize"


@dataclass
class LinearExpr:
    """A linear combination of decision variables plus a scalar constant."""

    _coeffs: dict[int, float] = field(default_factory=dict)
    _const: float = 0.0

    def __add__(self, other: LinearExpr | float) -> LinearExpr:
        if isinstance(other, (int, float)):
            return LinearExpr(dict(self._coeffs), self._const + other)
        coeffs = dict(self._coeffs)
        for col, c in other._coeffs.items():
            coeffs[col] = coeffs.get(col, 0.0) + c
        return LinearExpr(coeffs, self._const + other._const)

    def __radd__(self, other: float) -> LinearExpr:
        return self.__add__(other)

    def __sub__(self, other: LinearExpr | float) -> LinearExpr:
        if isinstance(other, (int, float)):
            return LinearExpr(dict(self._coeffs), self._const - other)
        return self.__add__(-1 * other)

    def __rsub__(self, other: float) -> LinearExpr:
        return (-1 * self).__add__(other)

    def __mul__(self, scalar: float) -> LinearExpr:
        return LinearExpr(
            {col: c * scalar for col, c in self._coeffs.items()},
            self._const * scalar,
        )

    def __rmul__(self, scalar: float) -> LinearExpr:
        return self.__mul__(scalar)

    def __neg__(self) -> LinearExpr:
        return self.__mul__(-1)

    # Comparison operators return Constraint objects, not booleans.
    # This is the standard pattern used by MILP modelling libraries (PuLP,
    # Gurobi, etc.).  LinearExpr is therefore unhashable by design.
    __hash__ = None  # type: ignore[assignment]

    def __eq__(self, other: LinearExpr | float) -> Constraint:  # type: ignore[override]
        return Constraint(self - other, lb=0.0, ub=0.0)

    def __le__(self, other: LinearExpr | float) -> Constraint:
        return Constraint(self - other, lb=-inf, ub=0.0)

    def __ge__(self, other: LinearExpr | float) -> Constraint:
        return Constraint(self - other, lb=0.0, ub=inf)


@dataclass(frozen=True)
class Constraint:
    """
    Represents lb <= expr <= ub, where expr is a LinearExpr whose variable
    part lives on the left-hand side (expr._const accounts for any constants
    moved from the right-hand side).
    """

    expr: LinearExpr
    lb: float
    ub: float


class MilpModel:
    """
    Lightweight MILP model builder that assembles and solves a problem using
    scipy.optimize.milp.

    Typical usage::

        model = MilpModel()
        x = model.add_variable(integer=True, lb=0, ub=1)
        y = model.add_variable(integer=True, lb=0)
        model.add_constraint(x + y >= 5)
        model.set_objective(x + 2 * y, sense=Sense.MINIMIZE)
        result = model.solve()

    """

    def __init__(self) -> None:
        self._num_vars: int = 0
        self._integer: list[bool] = []
        self._var_lb: list[float] = []
        self._var_ub: list[float] = []
        self._constraints: list[Constraint] = []
        self._objective: LinearExpr | None = None
        self._sense: Sense = Sense.MINIMIZE

    def add_variable(
        self,
        *,
        integer: bool = False,
        lb: float = 0.0,
        ub: float = inf,
    ) -> LinearExpr:
        """Register a new decision variable and return it as a LinearExpr."""
        col = self._num_vars
        self._num_vars += 1
        self._integer.append(integer)
        self._var_lb.append(lb)
        self._var_ub.append(ub)
        return LinearExpr({col: 1.0})

    def add_constraint(self, constraint: Constraint) -> None:
        """Add a constraint produced by ==, <= or >= on LinearExpr objects."""
        self._constraints.append(constraint)

    def set_objective(self, expr: LinearExpr, *, sense: Sense) -> None:
        """
        Set the objective function.

        Parameters
        ----------
        expr:
            Linear expression to optimise.
        sense:
            ``Sense.MINIMIZE`` or ``Sense.MAXIMIZE``.
        """
        self._objective = expr
        self._sense = Sense(sense)

    def solve(self) -> float:
        """
        Assemble and solve the model.  Returns the optimal objective value.
        Raises ``ValueError`` if the solver does not find an optimal solution.
        """
        n = self._num_vars

        # --- Objective vector ------------------------------------------------
        c = np.zeros(n)
        if self._objective is not None:
            for col, coeff in self._objective._coeffs.items():
                c[col] = coeff
        # scipy.milp always minimises; negate for maximisation
        if self._sense == Sense.MAXIMIZE:
            c = -c

        # --- Constraint matrix -----------------------------------------------
        m = len(self._constraints)
        if m > 0:
            A = np.zeros((m, n))
            lbs = np.empty(m)
            ubs = np.empty(m)
            for i, con in enumerate(self._constraints):
                for col, coeff in con.expr._coeffs.items():
                    A[i, col] = coeff
                # lb <= A_row * x + const <= ub
                # ⟺  lb - const <= A_row * x <= ub - const
                lbs[i] = con.lb - con.expr._const
                ubs[i] = con.ub - con.expr._const
            scipy_constraints: list = [LinearConstraint(A, lbs, ubs)]  # type: ignore
        else:
            scipy_constraints = []

        # --- Variable bounds and integrality ---------------------------------
        bounds = Bounds(lb=self._var_lb, ub=self._var_ub)  # type: ignore
        integrality = np.array(
            [1.0 if flag else 0.0 for flag in self._integer]
        )

        result = milp(
            c=c,
            constraints=scipy_constraints,
            integrality=integrality,
            bounds=bounds,
        )

        if result.status != 0:
            raise ValueError(f"MILP solve failed: {result.message}")

        obj_val: float = result.fun
        if self._sense == Sense.MAXIMIZE:
            obj_val = -obj_val
        return obj_val
