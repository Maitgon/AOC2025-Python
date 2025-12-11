# days/day11.py

import time
from pathlib import Path
from functools import cache

def read_input():
    day = Path(__file__).stem #day11
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"

    data = dict()

    for line in input_path.read_text().strip().splitlines():
        key, value = line.split(": ")
        data[key] = value.split(" ")
    
    return data


def part1(data):
    return dfs("you", "out", data)


def part2(data):
    return dfs("svr", "fft", data) * dfs("fft", "dac", data) * dfs("dac", "out", data)

def dfs(node_init: str, node_end: str, data: dict) -> int:
    
    @cache
    def dfs_cache(node: str) -> int:
        if node == node_end:
            return 1
        if node == "out":
            return 0
        count = 0
        for neighbor in data[node]:
            count += dfs_cache(neighbor)
        return count
    
    return dfs_cache(node_init)


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