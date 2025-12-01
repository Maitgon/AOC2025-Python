# days/day01.py

import time
from pathlib import Path

def read_input():
    day = Path(__file__).stem #day01
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return input_path.read_text().strip().splitlines()

def parts(data: list[str]):
    sol1 = 0
    sol2 = 0
    pos = 50

    for rotation in data:
        new_pos = pos
        if rotation[0] == "L":
            new_pos -= int(rotation[1:])
        elif rotation[0] == "R":
            new_pos += int(rotation[1:])

        if new_pos > 0:
            sol2 += abs(new_pos // 100)
        else:
            sol2 += abs((new_pos-1) // 100)
            if pos == 0:
                sol2 -= 1

        pos = new_pos % 100

        if pos == 0:
            sol1 += 1
    
    return sol1, sol2


def solve():
    start = time.perf_counter()

    # Input reading
    data = read_input()

    # Part 1 and 2
    sol1, sol2 = parts(data)

    t = (time.perf_counter() - start) * 1000

    print(f"Part 1: {sol1}")
    print(f"Part 2: {sol2}")
    print(f"Time  : {t:.3f} ms")