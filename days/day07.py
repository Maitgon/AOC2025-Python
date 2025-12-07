# days/day07.py

import time
from pathlib import Path

def read_input():
    day = Path(__file__).stem #day01
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return input_path.read_text().strip().splitlines()


def parts(data):
    sol1 = 0
    beams = dict([(s, 1) for s, c in enumerate(data[0]) if c == 'S'])
    for i in range(2, len(data), 2):
        new_beams = dict()
        for beam, n in beams.items():
            if data[i][beam] == '^':
                sol1 += 1
                new_beams[beam-1] = new_beams.get(beam-1, 0) + n
                new_beams[beam+1] = new_beams.get(beam+1, 0) + n
            else:
                new_beams[beam] = new_beams.get(beam, 0) + n
            
        beams = new_beams.copy()
    return sol1, sum(beams.values())


def solve():
    start = time.perf_counter()

    # Input reading
    data = read_input()

    # Part 1
    sol1, sol2 = parts(data)

    t = (time.perf_counter() - start) * 1000

    print(f"Part 1: {sol1}")
    print(f"Part 2: {sol2}")
    print(f"Time  : {t:.3f} ms")