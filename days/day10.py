# days/day10.py

import time
from pathlib import Path
from dataclasses import dataclass
from collections import deque
from ortools.sat.python import cp_model

@dataclass
class machine:
    final_state: tuple[int]
    buttons: list[list[int]]
    code: tuple[int]

    @classmethod
    def from_str(cls, s: str) -> "machine":
        try:
            parts = s.split(" ")
            final_state = []
            for aux in parts[0][1:-1]:
                if aux == '#':
                    final_state.append(1)
                else:
                    final_state.append(0)
            buttons = []
            for button_str in parts[1:-1]:
                button = []
                for aux in button_str[1:-1].split(","):
                    button.append(int(aux))
                buttons.append(button)
            code = []
            for aux in parts[-1][1:-1].split(","):
                code.append(int(aux))
        except ValueError:
            raise ValueError(f"Invalid Format: '{s}'. '[(#|.)+] ((n(,n)+) )+{{n(,n)+}}' expected.")
        return cls(tuple(final_state), buttons, tuple(code))

def read_input():
    day = Path(__file__).stem #day10
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return list(map(machine.from_str, input_path.read_text().strip().splitlines()))


def part1(data):
    sol1 = 0
    for m in data:
        sol1 += get_min_presses(m)
    return sol1

def get_min_presses(m: machine) -> int:
    starting_node = tuple([0]*len(m.final_state))
    
    queue = deque([(0, starting_node)])
    visited = set([starting_node])

    while queue:
        presses, state = queue.popleft()

        if state == m.final_state:
            return presses

        for button in m.buttons:
            new_node = list(state)
            for i in button:
                new_node[i] = 1 - new_node[i]
            new_node = tuple(new_node)
            if new_node not in visited:
                visited.add(new_node)
                queue.append((presses + 1, new_node))
    
    return 0
            


def part2(data):
    sol2 = 0
    for m in data:
        sol2 += smallest_presses(m)
    return sol2

def smallest_presses(m: machine) -> int:
    goal = list(m.code)
    start = [0]*len(m.final_state)
    n_buttons = len(m.buttons)

    model = cp_model.CpModel()

    # Create a model where the integer variables are between 0 and 10000
    x = [model.NewIntVar(0, 10000, f"x{i}") for i in range(n_buttons)]

    for i in range(len(start)):
        # Add a constraint
        model.Add(
            start[i] +
            sum(x[b] for b in range(n_buttons) if i in m.buttons[b])
            == goal[i]
        )

    # Objective function: minimize the sum of all variables
    model.Minimize(sum(x))

    solver = cp_model.CpSolver()
    solver.Solve(model)

    solution = [solver.Value(v) for v in x]
    return sum(solution)

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