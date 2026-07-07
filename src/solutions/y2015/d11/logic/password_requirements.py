from typing import Callable


def has_three_increasing_straight(password: str) -> bool:
    ords = [ord(c) for c in password]
    for i in range(len(ords) - 2):
        if ords[i] + 1 == ords[i + 1] and ords[i] + 2 == ords[i + 2]:
            return True
    return False


def has_no_forbidden_letters(password: str) -> bool:
    return all(letter not in password for letter in "iol")


def has_two_different_pairs(password: str) -> bool:
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2


def _increment(password: str) -> str:
    password_list = list(password)
    index = len(password_list) - 1

    while index >= 0:
        if password_list[index] == "z":
            if index == 0:
                raise OverflowError("No more possible passwords")
            password_list[index] = "a"
            index -= 1
        else:
            password_list[index] = chr(ord(password_list[index]) + 1)
            break

    return "".join(password_list)


def next_valid_password(
    password: str, requirements: list[Callable[[str], bool]]
) -> str:
    candidate = _increment(password)

    while not all(requirement(candidate) for requirement in requirements):
        candidate = _increment(candidate)

    return candidate
