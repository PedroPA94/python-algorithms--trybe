from typing import List, Tuple


def study_schedule(
    permanence_period: List[Tuple[int, int]], target_time: int
) -> int:
    if not isinstance(target_time, int):
        return None

    counter = 0

    for student_permanence_period in permanence_period:
        (entry_time, exit_time) = student_permanence_period

        if not isinstance(entry_time, int) or not isinstance(exit_time, int):
            return None

        if entry_time <= target_time <= exit_time:
            counter += 1

    return counter
