# days/day08.py

import time
from pathlib import Path

from dataclasses import dataclass

@dataclass
class point3d:
    x: int
    y: int
    z: int

    @classmethod
    def from_str(cls, s: str) -> "point3d":
        try:
            x, y, z = s.split(",")
        except ValueError:
            raise ValueError(f"Invalid Format: '{s}'. 'x,y,z' expected.")
        return cls(int(x), int(y), int(z))
    
    def euclidean_distance(self, other: "point3d") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))

def read_input():
    day = Path(__file__).stem #day08
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return list(map(point3d.from_str, input_path.read_text().strip().splitlines()))


def part1(data: list[point3d]):
    distances = dict()
    for i in range(0, len(data)):
        p1 = data[i]
        for j in range(i+1, len(data)):
            p2 = data[j]
            dist = p1.euclidean_distance(p2)
            if dist <= 20000:
                distances[(p1, p2)] = dist

    sorted_distances = sorted(distances.items(), key=lambda item: item[1])

    return kruskal(data, sorted_distances[:20000])

def kruskal(points: list[point3d], distances: list[tuple[tuple[point3d, point3d], float]]) -> tuple[int, int]:
    F = []
    edge_count = 1

    def find(p: point3d) -> set:
        for s in F:
            if p in s:
                return s
        
        return set()

    def union(s1: set, s2: set) -> set:
        return s1.union(s2)

    for p in points:
        F.append(set([p]))
    
    for (u, v), _ in distances:
        fu = find(u)
        fv = find(v)
        if fu != fv:
            F.remove(fu)
            F.remove(fv)
            F.append(union(fu, fv))
        
        if edge_count == 1000:
            clusters_size = sorted(map(len, F))
            sol1 = clusters_size[-1] * clusters_size[-2] * clusters_size[-3]
        edge_count += 1
        
        if len(F) == 1:
            return sol1, u.x * v.x
    
    return 0, 0


def solve():
    start = time.perf_counter()

    # Input reading
    data = read_input()

    # Part 1
    sol1, sol2 = part1(data)

    t = (time.perf_counter() - start) * 1000

    print(f"Part 1: {sol1}")
    print(f"Part 2: {sol2}")
    print(f"Time  : {t:.3f} ms")