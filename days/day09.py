# days/day09.py

import time
from pathlib import Path
from dataclasses import dataclass
from shapely.geometry.polygon import Polygon

@dataclass
class point:
    x: int
    y: int

    @classmethod
    def from_str(cls, s: str) -> "point":
        try:
            x, y= s.split(",")
        except ValueError:
            raise ValueError(f"Invalid Format: '{s}'. 'x,y' expected.")
        return cls(int(x), int(y))

    def area(self, other: "point") -> int:
        return (abs(self.x - other.x)+1) * (abs(self.y - other.y) + 1)

def read_input():
    day = Path(__file__).stem #day09
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return list(map(point.from_str, input_path.read_text().strip().splitlines()))


def part1(data: list[point]):
    sol1 = 0
    for i in range(0, len(data)):
        p1 = data[i]
        for j in range(i+1, len(data)):
            p2 = data[j]
            area = p1.area(p2)
            if area > sol1:
                sol1 = area
    return sol1

def part2(data):
    sol2 = 0
    poly = Polygon([(p.x, p.y) for p in data])
    relevant_points = [i+1 for i in range(0, len(data)-1) if abs(data[i].x - data[i+1].x) > 50000 or abs(data[i].y - data[i+1].y) > 50000]
    relevant_points[-1] = relevant_points[0] + 1

    for i in relevant_points[:-1]:
        p1 = data[i]
        for j in range(0, len(data)):
            p2 = data[j]
            area = p1.area(p2)
            if area < sol2:
                continue
            
            if poly.contains(Polygon([(p1.x, p1.y), (p2.x, p1.y), (p2.x, p2.y), (p1.x, p2.y)])):
                sol2 = area
                
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