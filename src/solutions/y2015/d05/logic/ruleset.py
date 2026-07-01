from typing import Callable


def is_nice(text: str, ruleset: list[Callable[[str], bool]]) -> bool:
    return all(rule(text) for rule in ruleset)


first_ruleset = [
    lambda text: sum(text.count(vowel) for vowel in "aeiou") >= 3,
    lambda text: any(text[i] == text[i + 1] for i in range(len(text) - 1)),
    lambda text: not any(
        substring in text for substring in ["ab", "cd", "pq", "xy"]
    ),
]

second_ruleset = [
    lambda text: any(
        text[i : i + 2] in text[i + 2 :] for i in range(len(text) - 1)
    ),
    lambda text: any(text[i] == text[i + 2] for i in range(len(text) - 2)),
]
