def optimize_joltage(batteries: tuple[int, ...]) -> int:
    first_digit = max(batteries[:-1])
    first_digit_idx = batteries.index(first_digit)
    second_digit = max(batteries[first_digit_idx + 1 :])
    return 10 * first_digit + second_digit
