from src.solutions.shared.optimization.milp_model import MilpModel, Sense


def test_minimize_single_variable():
    model = MilpModel()
    x = model.add_variable(integer=True, lb=0)
    model.add_constraint(x >= 3)
    model.set_objective(x, sense=Sense.MINIMIZE)
    assert model.solve() == 3.0


def test_maximize_single_variable():
    model = MilpModel()
    x = model.add_variable(integer=True, lb=0)
    model.add_constraint(x <= 7)
    model.set_objective(x, sense=Sense.MAXIMIZE)
    assert model.solve() == 7.0


def test_equality_constraint():
    model = MilpModel()
    x = model.add_variable(integer=True, lb=0)
    model.add_constraint(x == 5)
    model.set_objective(x, sense=Sense.MINIMIZE)
    assert model.solve() == 5.0


def test_variable_upper_bound():
    model = MilpModel()
    x = model.add_variable(integer=True, lb=0, ub=4)
    model.set_objective(x, sense=Sense.MAXIMIZE)
    assert model.solve() == 4.0


def test_sum_of_variables():
    model = MilpModel()
    x = [model.add_variable(integer=True, lb=0) for _ in range(4)]
    model.add_constraint(sum(x) >= 10)  # type: ignore
    model.set_objective(sum(x), sense=Sense.MINIMIZE)  # type: ignore
    assert model.solve() == 10.0


def test_two_variable_maximization():
    model = MilpModel()
    x = model.add_variable(integer=True, lb=0)
    y = model.add_variable(integer=True, lb=0)
    model.add_constraint(2 * x + y <= 10)
    model.add_constraint(x + 2 * y <= 10)
    model.set_objective(x + y, sense=Sense.MAXIMIZE)
    assert model.solve() == 6.0


def test_constraint_with_rhs_constant():
    model = MilpModel()
    x = model.add_variable(integer=True, lb=0)
    y = model.add_variable(integer=True, lb=0)
    model.add_constraint(x + y == 8)
    model.add_constraint(x >= 3)
    model.set_objective(x, sense=Sense.MINIMIZE)
    assert model.solve() == 3.0
