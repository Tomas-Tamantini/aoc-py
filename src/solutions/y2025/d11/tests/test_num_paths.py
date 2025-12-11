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
    assert num_paths(origin="you", destination="out", adjacencies=adjacencies)
