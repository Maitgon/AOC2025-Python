# days/day03.py

import time
from pathlib import Path
from functools import reduce

def read_input():
    day = Path(__file__).stem #day03
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return input_path.read_text().strip().splitlines()


def part1(data):
    sol1 = 0
    for seq in data:
        d = 0
        u = 0
        i = 0

        for j, val in enumerate(seq[:len(seq)-1]):
            if int(val) > d:
                d = int(val)
                i = j
            if d == 9:
                break
        
        for val in seq[i+1:]:
            if int(val) > u:
                u = int(val)
            if u == 9:
                break
        
        sol1 += d*10 + u
    
    return sol1

def part2(data):
    sol2 = 0
    for seq in data:
        vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        i = -1
        for digit in range(11, -1, -1):
            for j in range(i+1,len(seq)-digit):
                if int(seq[j]) > vals[digit]:
                    vals[digit] = int(seq[j])
                    i = j
                if vals[digit] == 9:
                    break

        sol2 += sum([d * (10 ** i) for i, d in enumerate(vals)])
    
    return sol2


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