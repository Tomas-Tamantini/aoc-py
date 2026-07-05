# Copilot Instructions

This is a Python project containing solutions to [Advent of Code](https://adventofcode.com/) problems.

## Project layout

```
src/
  solutions/
    shared/          # Reusable utilities shared across solutions
    y{year}/
      d{day:02d}/
        solution.py  # Entry point: solve(io_handler) -> None
        logic/       # Optional: parsing and algorithm modules
        tests/       # Unit tests for logic/parser modules
        data/
          input.txt
          results.json
  core/              # IOHandler, InputReader, etc.
  cli/               # CLI implementation (don't modify)
  scripts/           # setup_solution.py scaffold script
main.py
```

## Scaffolding a new solution

```bash
task setup_solution -y 2025 -d 1
```

This creates the folder structure and a stub `solution.py`.

## Solution entry point

Every solution must have exactly one public function:

```python
from src.core.io_handler import IOHandler

def solve(io_handler: IOHandler) -> None:
    prob_id = 2025, 1

    # Read puzzle input
    reader = io_handler.input_reader(*prob_id)

    io_handler.write_result(*prob_id, part=1, result=42)
    io_handler.write_result(*prob_id, part=2, result=99)
```

- `prob_id` is always `(year, day)` as a tuple literal at the top of `solve`.
- `io_handler.write_result` always receives `*prob_id, part=N, result=value`.

## Splitting logic

- For simple problems, parsing and logic can live directly in `solution.py`.
- For more complex problems, split into files under `logic/` (e.g. `parser.py`, `algorithm.py`).
- Import from `logic/` into `solution.py`; keep `solution.py` thin.

## InputReader

```python
reader.read_input()                          # full raw string
reader.read_lines()                          # iterator of lines (with newlines)
reader.read_stripped_lines()                 # iterator of stripped, non-empty lines
reader.read_stripped_lines(keep_empty_lines=True)
```

## Shared utilities

Always prefer these over re-implementing from scratch:

### Graph — `from src.solutions.shared.graph import ...`

- `bfs(start, neighbors)` / `min_path_length_with_bfs(...)`
- `dfs(start, neighbors)`
- `min_path_length_with_dijkstra(...)`
- `DisjointSet`
- `UndirectedGraph[T]`, `WeightedUndirectedGraph[T]`

### Geometry — `from src.solutions.shared.geometry import ...`

- `Vector2D`, `Vector3D`
- `Direction`, `Turn`
- `BoundingBox`
- `HexagonalCoordinates`, `HexagonalDirection`

### Parser — `from src.solutions.shared.parser import ...`

- `CharacterGrid`, `GridParser`, `CsvParser`, `DirectionParser`

### VM — `from src.solutions.shared.vm import ...`

For problems involving a custom assembly-like computer (common in 2019).

### Other

- `src.solutions.shared.number_theory.interval` — `Interval`
- `src.solutions.shared.optimization.milp_model` — MILP via scipy

## Testing

- Tests live in `tests/` inside the solution folder.
- Use the shared `input_reader` fixture (from `src/solutions/conftest.py`) to test parsers:

```python
from typing import Callable
from src.core.input_reader import InputReader

def test_my_parser(input_reader: Callable[[str], InputReader]) -> None:
    example = "some\ninput"
    result = my_parser(input_reader(example))
    assert result == expected
```

- Test logic modules directly — never test through the `IOHandler`.
- No test file should import from `solution.py`.

## Tooling

| Command                             | Purpose                         |
| ----------------------------------- | ------------------------------- |
| `task run`                          | Run all solutions               |
| `task run -y 2022 -d 5`             | Run a specific solution         |
| `task run -a`                       | Run with animations             |
| `task run -i`                       | Run in interactive mode         |
| `task run -p tom`                   | Use `data/tom/` as input folder |
| `task test`                         | Run all tests with coverage     |
| `task format`                       | Format & lint with ruff         |
| `task setup_solution -y YYYY -d DD` | Scaffold new solution           |

- Package manager: `uv`. Do not use `pip` directly.
- Python version: see `.python-version`.
- Linter/formatter: `ruff` (line length 79, preview mode, rules: I, F, E, W, PL, PT).
