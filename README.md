# AOC-PY

Solutions to the [Advent of Code](https://adventofcode.com/) challenges.

## Important commands

With the virtual environment activated, run the following commands:

### Running Solutions

Run all solutions:

```bash
task run
```

Run solutions for a specific year:

```bash
task run --year 2022
task run -y 2022
```

Run solutions for a specific day across all years:

```bash
task run --day 1
task run -d 1
```

Run a specific solution:

```bash
task run --year 2022 --day 1
task run -y 2022 -d 1
```

Run with animations (for supported solutions):

```bash
task run --animate
task run -a
```

Run in interactive game mode (for supported solutions):

```bash
task run --interactive
task run -i
```

Combine flags for specific solutions with special features:

```bash
task run --year 2019 --day 13 --animate
task run -y 2019 -d 25 -a -i
```

Get help:

```bash
task run --help
```

### Testing

```bash
task test
```

### Formatting

```bash
task format
```

### Setting up file structure for a new solution

```bash
task setup_solution -y 2099 -d 1
```
