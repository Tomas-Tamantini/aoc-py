from src.solutions.shared.optimization.milp_model import MilpModel, Sense
from src.solutions.y2022.d19.logic.blueprint import Blueprint
from src.solutions.y2022.d19.logic.resource import ResourceType

"""
MILP modeling

Notation:
    - Nat = Natural numbers including zero

Indices:
    - Resource type:
        - r in {ORE, CLAY, OBSIDIAN, GEODE}
    - Timestamp in minutes
        - t in [0..TIME_LIMIT]

Constants:
    - Initial <F>leet size of robot of type r:
        - F_r in Nat
    - Cost in resource r to <B>uild robot of type r':
        - B_{r, r'} in Nat

Variables:
    - <f>leet size of robot of type r at the beginning of minute t:
        - f_{r, t} in Nat
    - Inventory <a>mount of resource r at the beginning of minute t:
        - a_{r, t} in Nat
    - <E>xpenditure of resource r at minute t by robot factory:
        - e_{r, t} in Nat
    - Decision variable, whether robot of type r gets built at minute t:
        - x_{r, t} in {0, 1}

Objective function:
    - Maximize given resource at the end of the time limit:
        - max a_{r=RESOURCE_TO_MAXIMIZE, t=TIME_LIMIT}

Constraints:
    - Initial inventory empty:
        - a_{r, t=0} = 0 forall r
    - Initial fleet size given:
        - f_{r, t=0} = F_r forall r
    - At most one robot built per minute:
        - sum_r x_{r, t} <= 1 forall t
    - Fleet size gets incremented by built robots:
        - f_{r, t+1} = f_{r, t} + x_{r, t} forall r, for t in [0, TIME_LIMIT-1]
    - Definition of e_{r, t} (Resource expenditure by factory):
        - e_{r, t} = sum_r' x_{r', t} * B_{r', r}
    - There must be enough resources to start building robot:
        - a_{r, t} >= e_{r, t} forall t, r
    - Inventory gets incremented by existing fleet and decremented by factory:
        - a_{r, t+1} = a_{r, t} + f_{r, t} - e_{r, t}
            forall r, for t in [0, TIME_LIMIT-1]
"""


def maximize_resource(
    resource_to_maximize: ResourceType,
    time_limit: int,
    blueprint: Blueprint,
    initial_fleet: dict[ResourceType, int],
) -> int:
    R = list(ResourceType)
    T = time_limit

    model = MilpModel()
    x = {
        (r, t): model.add_variable(integer=True, lb=0, ub=1)
        for r in R
        for t in range(T)
    }
    f = {
        (r, t): model.add_variable(integer=True, lb=0)
        for r in R
        for t in range(T + 1)
    }
    a = {
        (r, t): model.add_variable(integer=True, lb=0)
        for r in R
        for t in range(T + 1)
    }
    e = {
        (r, t): model.add_variable(integer=True, lb=0)
        for r in R
        for t in range(T)
    }

    for r in R:
        model.add_constraint(a[r, 0] == 0)
        model.add_constraint(f[r, 0] == initial_fleet.get(r, 0))
        for t in range(T):
            cost_expr = sum(
                x[r2, t] * blueprint.costs.get(r2, {}).get(r, 0) for r2 in R
            )
            model.add_constraint(e[r, t] == cost_expr)
            model.add_constraint(f[r, t + 1] == f[r, t] + x[r, t])
            model.add_constraint(a[r, t + 1] == a[r, t] + f[r, t] - e[r, t])
            model.add_constraint(a[r, t] >= e[r, t])

    for t in range(T):
        model.add_constraint(sum(x[r, t] for r in R) <= 1)  # type: ignore

    model.set_objective(a[resource_to_maximize, T], sense=Sense.MAXIMIZE)
    return round(model.solve())
