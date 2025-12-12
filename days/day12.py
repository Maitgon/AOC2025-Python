# days/day12.y

import time
from pathlib import Path

def read_input():
    day = Path(__file__).stem #day12
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    aux = input_path.read_text().strip().split("\n\n")
    input = []
    for line in aux[-1].splitlines():
        line_input = []
        line_aux = line.split(" ")
        aux2 = line_aux[0][:-1].split("x")
        line_input.append(int(aux2[0]))
        line_input.append(int(aux2[1]))
        for item in line_aux[1:]:
            line_input.append(int(item))
        input.append(line_input.copy())
    return input

def part1(data):
    sol1 = 0
    for tree in data:
        total_area = tree[0] * tree[1]
        for num in tree[2:]:
            total_area -= 9 * num
        sol1 += 1 if total_area >= 0 else 0
    return sol1

def solve():
    start = time.perf_counter()

    # Input reading
    data = read_input()

    # Part 1
    sol1 = part1(data)

    t = (time.perf_counter() - start) * 1000

    print(f"Part 1: {sol1}")
    print(f"Part 2: All I want for Christmas is you!")
    print(f"Time  : {t:.3f} ms")