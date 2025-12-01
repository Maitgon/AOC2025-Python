# main.py

import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(description="Run an Advent of Code day.")
    parser.add_argument(
        "day",
        type=int,
    )

    args = parser.parse_args()
    day_num = args.day

    module_name = f"days.day{day_num:02d}"

    try:
        day_module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"File for day {day_num:02d} does not exists.")
        return

    print(f"--- Advent of Code — Day {day_num:02d} ---")
    day_module.solve()


if __name__ == "__main__":
    main()