from time import sleep


class CLIGameInterface:
    def __init__(self, year: int, day: int, part: int) -> None:
        self._year = year
        self._day = day
        self._part = part

    @staticmethod
    def prompt_input() -> str:
        return input()

    @staticmethod
    def put_character(char: str) -> None:
        print(char, end="")

    @staticmethod
    def put_string(text: str, delay_ms: int = 0) -> None:
        print(text)
        if delay_ms:
            sleep(delay_ms / 1000)
