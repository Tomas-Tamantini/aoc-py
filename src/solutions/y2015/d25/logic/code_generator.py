def get_code_at(row: int, col: int) -> int:
    """
    Calculates the code at a given row and column in the grid.
    """
    position = (row + col - 2) * (row + col - 1) // 2 + col

    code = 20151125
    multiplier = 252533
    divisor = 33554393

    for _ in range(1, position):
        code = (code * multiplier) % divisor

    return code
