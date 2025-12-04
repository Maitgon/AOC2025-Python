# days/day04.py

import time
from pathlib import Path

Dirs = [(1,1),  (1,0),  (1,-1),
        (0,1),          (0,-1),
        (-1,1), (-1,0), (-1,-1)]

def read_input():
    day = Path(__file__).stem #day04
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return input_path.read_text().strip().splitlines()

def count_rolls(i, j, rolls):
    c = 0
    for di, dj in Dirs:
        if (i + di, j + dj) in rolls:
            c += 1
    return c


def part1(data):
    sol1 = 0

    rolls = {(i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == '@'}
    sol1 = 0
    for i, j in rolls:
        if count_rolls(i, j, rolls) < 4:
            sol1 += 1
    return sol1


def part2(data):
    rolls = {(i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == '@'}
    sol = 0

    queue = set(rolls)

    while queue:
        new_queue = set()
        for i, j in queue:
            if (i, j) not in rolls:
                continue

            if count_rolls(i, j, rolls) < 4:
                sol += 1
                rolls.remove((i, j))

                # neighbors might now change eligibility
                for di, dj in Dirs:
                    n = (i + di, j + dj)
                    if n in rolls:
                        new_queue.add(n)

        queue = new_queue

    return sol



def solve():
    start = time.perf_counter()

    # Input reading
    data = read_input()

    # Part 1
    sol1 = part1(data)

    # Part 2
    sol2 = part2(data)

    t = (time.perf_counter() - start) * 1000

    print(f"Part 1: {sol1}")
    print(f"Part 2: {sol2}")
    print(f"Time  : {t:.3f} ms")