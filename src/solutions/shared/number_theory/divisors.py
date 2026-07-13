def sum_of_divisors(n: int) -> int:
    total_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total_sum += i
            if i != n // i:
                total_sum += n // i
    return total_sum


def divisors(n: int) -> set[int]:
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs
