from dataclasses import dataclass


@dataclass(frozen=True)
class CephalopodMathProblem:
    numbers: tuple[int, ...]
    operator: str

    def evaluate(self) -> int:
        return eval(self.operator.join(map(str, self.numbers)))
