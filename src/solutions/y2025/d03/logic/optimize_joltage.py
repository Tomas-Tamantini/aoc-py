def optimize_joltage(batteries: tuple[int, ...], num_digits: int) -> int:
    if num_digits == 1:
        return max(batteries)
    max_digit = max(batteries[: -(num_digits - 1)])
    max_digit_idx = batteries.index(max_digit)
    remaining = optimize_joltage(
        batteries[max_digit_idx + 1 :], num_digits=num_digits - 1
    )
    return 10 ** (num_digits - 1) * max_digit + remaining
