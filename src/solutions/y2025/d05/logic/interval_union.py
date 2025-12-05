from src.solutions.shared.number_theory.interval import Interval


def union_size(intervals: list[Interval]) -> int:
    remaining = sorted(intervals, reverse=True)
    size = 0
    while remaining:
        interval = remaining.pop()
        if remaining and (joined := remaining[-1].union(interval)):
            remaining.pop()
            remaining.append(joined)
        else:
            size += interval.size
    return size
