# days/day06.py

import time
from pathlib import Path
from functools import reduce

def read_input():
    day = Path(__file__).stem #day01
    input_path = Path(__file__).parents[1] / "inputs" / f"{day}.txt"
    return input_path.read_text().strip().splitlines()


def part1(data):
    data = [line.split() for line in data]
    sol1 = 0
    for j in range(0, len(data[0])):
        nums = [int(pos[j]) for pos in data[0:-1]]
        operand = data[-1][j]
        if operand == '+':
            sol1 += reduce(lambda x, y: x + y, nums, 0)
        elif operand == '*':
            sol1 += reduce(lambda x, y: x * y, nums, 1)
    return sol1



def part2(data):
    operands = data[-1].split()
    sol2 = 0
    op = 0
    nums = []
    for j in range(0, len(data[0])):
        pos_num = ""
        # Get the column number
        for i in range(0, len(data)-1):
            if data[i][j] != " ":
                pos_num += data[i][j]
        
        # If the column number is all whitespace, the the numbers end, and you operate them
        # Also if it is the last column
        if pos_num == "" or j == len(data[0])-1:
            if j == len(data[0])-1:
                nums.append(int(pos_num))
            operand = operands[op]
            if operand == '+':
                sol2 += reduce(lambda x, y: x + y, nums, 0)
            elif operand == '*':
                sol2 += reduce(lambda x, y: x * y, nums, 1)
            nums = []
            op += 1
        
        # If the column contains some number, delete the whitespace and add the number
        else:
            nums.append(int(pos_num))
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