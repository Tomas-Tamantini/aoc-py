from src.solutions.y2025.d11.logic.num_paths import num_paths


def test_num_paths_in_dag_is_calculated_properly():
    adjacencies = {
        "aaa": {"you", "hhh"},
        "you": {"bbb", "ccc"},
        "bbb": {"ddd", "eee"},
        "ccc": {"ddd", "eee", "fff"},
        "ddd": {"ggg"},
        "eee": {"out"},
        "fff": {"out"},
        "ggg": {"out"},
        "hhh": {"ccc", "fff", "iii"},
        "iii": {"out"},
    }
    assert num_paths("you", "out", adjacencies=adjacencies) == 5


def test_num_paths_in_dag_is_calculated_efficiently():
    adjacencies = {i: (i + 1, i + 2) for i in range(50)}
    assert num_paths(0, 49, adjacencies=adjacencies) == 12586269025


def test_path_may_have_intermediate_points():
    adjacencies = {i: (i + 1, i + 2) for i in range(50)}
    assert num_paths(0, 25, 30, 49, adjacencies=adjacencies) == 6569789160
    assert num_paths(0, 25, 20, 49, adjacencies=adjacencies) == 0
