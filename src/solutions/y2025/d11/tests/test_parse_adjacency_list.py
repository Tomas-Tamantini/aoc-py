from src.solutions.y2025.d11.logic.parser import parse_adjacency_list


def test_parse_adjacency_list(input_reader):
    reader = input_reader(
        """
        aaa: bbb ccc
        ccc: ddd eee fff
        ddd: eee
        """
    )
    adjacencies = parse_adjacency_list(reader)
    assert adjacencies == {
        "aaa": ("bbb", "ccc"),
        "ccc": ("ddd", "eee", "fff"),
        "ddd": ("eee",),
    }
