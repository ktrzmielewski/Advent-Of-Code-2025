import sys
import os
from days_registry import FINISHED_DAYS, NUM_OF_DAYS

sys.path.append(os.path.dirname(__file__))

def run_day(n: int):
    if n not in FINISHED_DAYS:
        print(f"No solution registered for day {n}.")
        return False
    day_class = FINISHED_DAYS[n]
    day_instance = day_class()
    try:
        return day_instance.solve_and_get_results()
    except NotImplementedError:
        print(f"Day {n} solution not finished yet.")
        return False


def run_and_calculate_num_of_solved_days():
    solved_count = 0
    for n in range(1, NUM_OF_DAYS + 1):
        result = run_day(n)
        if result is True:
            solved_count += 1
    return solved_count


def draw_christmas_tree(num_solved):
    if num_solved == 0:
        print("No stars yet… solve some days! ❄️")
        return

    print(f"\n🎄 Solved {num_solved} days 🎄")
    print("🎄 Your Advent Tree 🎄\n")

    for row in range(1, num_solved + 1):
        stars = "*" * (2 * row - 1)
        padding = " " * (num_solved - row)
        print(padding + stars + padding)


if __name__ == '__main__':
    solved_days_count = run_and_calculate_num_of_solved_days()
    draw_christmas_tree(solved_days_count)

