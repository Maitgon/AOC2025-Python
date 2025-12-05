# days/day01.y

import time
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Pair:
    x: int
    y: int

    @classmethod
    def from_str(cls, s: str) -> "Pair":
        try:
            x, y = s.split("-")
        except ValueError:
            raise ValueError(f"Invalid Format: '{s}'. 'x-y' expected.")
        return cls(int(x), int(y))

def read_input():
    day = Path(__file__).stem #day01
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    split2 = input_path.read_text().strip().split("\n\n")
    return (list(map(Pair.from_str, split2[0].splitlines())), list(map(int, split2[1].splitlines())))

def parts(data):
    sort_data = sorted(data[0], key=lambda p: p.x)
    union = [sort_data[0]]

    for pair in sort_data[1:]:
        last = union[-1]
        if pair.x <= last.y:
            last.y = max(last.y, pair.y)
        else:
            union.append(pair)
    
    sol1 = 0
    for id in data[1]:
        l, r = 0, len(union) - 1
        found = False
        while l <= r:
            m = (l + r) // 2
            pair = union[m]
            if pair.x <= id <= pair.y:
                found = True
                break
            elif id < pair.x:
                r = m - 1
            else:
                l = m + 1
        if found:
            sol1 += 1
    
    return sol1, sum(p.y - p.x + 1 for p in union)


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