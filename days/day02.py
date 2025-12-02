# days/day02.py

import time
from pathlib import Path
from dataclasses import dataclass
import math
from days.utils import divisors


@dataclass
class Pair:
    x: str
    y: str

    @classmethod
    def from_str(cls, s: str) -> "Pair":
        try:
            x, y = s.split("-")
        except ValueError:
            raise ValueError(f"Invalid Format: '{s}'. 'x-y' expected.")
        return cls(x, y)

def read_input():
    day = Path(__file__).stem #day02
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return list(map(Pair.from_str, input_path.read_text().strip().split(',')))


def part1(data):
    invalid_ids = []
    for p in data:
        nx, ny = '', ''
        if len(p.x) == len(p.y) and len(p.x) % 2 == 0:
            nx, ny = p.x, p.y
        elif len(p.x) != len(p.y): # So the len of p.x is len(p.y)-1
            if len(p.x) % 2 == 0:
                nx, ny = p.x, '9'*len(p.x)
            else:
                nx, ny = '1' + '0'*(len(p.y)-1), p.y
        else:
            continue
        
        for id in range(int(nx[0:len(nx)//2]), int(ny[0:len(ny)//2])+1):
            if int(p.x) <= int(str(id)+str(id)) and int(str(id)+str(id)) <= int(p.y):
                invalid_ids.append(int(str(id)+str(id)))

    return sum(invalid_ids)


def part2(data):
    invalid_ids = []
    for p in data:
        nx, ny = p.x, p.y

        divisors_check = set()
        divisors_check = set(divisors(len(nx)) + divisors(len(ny)))
        divisors_check.discard(1)
        
        for n in divisors_check:
            for id in range(inte(nx[0:math.floor(len(nx)/n)]), inte(ny[0:math.ceil(len(ny)/n)])+1):
                if int(p.x) <= int(str(id)*n) and int(str(id)*n) <= int(p.y):
                    invalid_ids.append(int(str(id)*n))

    return sum(set(invalid_ids))

def inte(s):
    if s == '':
        return 0
    else:
        return int(s)


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