from os.path import join
from typing import Iterator, Optional


class TextFileInputReader:
    def __init__(
        self,
        year: int,
        day: int,
        file_name: Optional[str] = None,
        profile: Optional[str] = None,
    ):
        file_name = file_name or "input.txt"
        path_elements = ["src", "solutions", f"y{year}", f"d{day:02d}", "data"]
        if profile:
            path_elements.append(profile)
        path_elements.append(file_name)
        self._file_path = join(*path_elements)

    def read_input(self) -> str:
        with open(self._file_path, "r", encoding="utf-8") as file:
            return file.read()

    def read_lines(self) -> Iterator[str]:
        with open(self._file_path, "r", encoding="utf-8") as file:
            for line in file:
                yield line

    def read_stripped_lines(
        self, keep_empty_lines: bool = False
    ) -> Iterator[str]:
        for line in self.read_lines():
            stripped = line.strip()
            if stripped or keep_empty_lines:
                yield line.strip()
