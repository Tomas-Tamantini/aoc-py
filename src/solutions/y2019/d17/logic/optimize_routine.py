from typing import Iterator

from src.solutions.y2019.d17.logic.memory_specs import VacuumRobotMemorySpecs


class CompressedRoutine:
    def __init__(
        self,
        main_movement_routine: list[str],
        movement_functions: dict[str, list[str]],
    ) -> None:
        self._main_movement_routine = main_movement_routine
        self._movement_functions = movement_functions

    @property
    def main_movement_routine(self) -> str:
        return ",".join(self._main_movement_routine)

    def movement_functions(self) -> Iterator[str]:
        for key in sorted(self._movement_functions.keys()):
            yield ",".join(self._movement_functions[key])

    def max_string_length(self) -> int:
        return max(
            len(self.main_movement_routine),
            *(len(f) for f in self.movement_functions()),
        )


class _PartialSolution:
    def __init__(
        self,
        main_routine: list[str],
        subroutines: dict[str, list[str]],
        remaining_instructions: list[str],
    ) -> None:
        self._main_routine = main_routine
        self._subroutines = subroutines
        self._remaining_instructions = remaining_instructions

    @property
    def is_complete(self) -> bool:
        return not self._remaining_instructions

    def as_compressed_routine(self) -> CompressedRoutine:
        return CompressedRoutine(
            main_movement_routine=self._main_routine,
            movement_functions=self._subroutines,
        )

    def _add_subroutine(self, subroutine_size: int) -> "_PartialSolution":
        new_subroutine = self._remaining_instructions[:subroutine_size]
        new_sub_name = chr(ord("A") + len(self._subroutines))
        return _PartialSolution(
            main_routine=self._main_routine + [new_sub_name],
            subroutines={**self._subroutines, new_sub_name: new_subroutine},
            remaining_instructions=self._remaining_instructions[
                subroutine_size:
            ],
        )

    def _subroutine_matches_next_block(self, subroutine_name: str) -> bool:
        subroutine = self._subroutines[subroutine_name]
        return subroutine == self._remaining_instructions[: len(subroutine)]

    def _use_subroutine(self, subroutine_name: str) -> "_PartialSolution":
        subroutine_size = len(self._subroutines[subroutine_name])
        return _PartialSolution(
            main_routine=self._main_routine + [subroutine_name],
            subroutines=self._subroutines,
            remaining_instructions=self._remaining_instructions[
                subroutine_size:
            ],
        )

    def _use_existing_subroutines(self) -> Iterator["_PartialSolution"]:
        for sub_name in self._subroutines:
            if self._subroutine_matches_next_block(sub_name):
                yield self._use_subroutine(sub_name)

    def _create_new_subroutine(self) -> Iterator["_PartialSolution"]:
        for subroutine_size in range(1, len(self._remaining_instructions) + 1):
            yield self._add_subroutine(subroutine_size)

    def neighbor_states(
        self, total_num_subroutines: int
    ) -> Iterator["_PartialSolution"]:
        yield from self._use_existing_subroutines()
        if len(self._subroutines) < total_num_subroutines:
            yield from self._create_new_subroutine()


class _RoutineGenerator:
    def __init__(self, memory_specs: VacuumRobotMemorySpecs) -> None:
        self._memory_specs = memory_specs

    def _solution_is_valid(self, solution: CompressedRoutine) -> bool:
        return (
            solution.max_string_length() <= self._memory_specs.max_characters
        )

    def _generate_routines(
        self, partial: _PartialSolution
    ) -> Iterator[CompressedRoutine]:
        if partial.is_complete:
            yield partial.as_compressed_routine()
        else:
            for neighbor in partial.neighbor_states(
                self._memory_specs.num_subroutines
            ):
                yield from self._generate_routines(neighbor)

    def compressed_routines(
        self, instructions: list[str]
    ) -> Iterator[CompressedRoutine]:
        initial = _PartialSolution(
            main_routine=[],
            subroutines=dict(),
            remaining_instructions=instructions,
        )
        for solution in self._generate_routines(initial):
            if self._solution_is_valid(solution):
                yield solution


def optimize_routine(
    instructions: list[str], memory_specs: VacuumRobotMemorySpecs
) -> CompressedRoutine:
    generator = _RoutineGenerator(memory_specs)
    return next(generator.compressed_routines(instructions))
