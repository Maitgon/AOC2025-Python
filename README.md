<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=8A2BE2&text=Advent%20of%20Code%202025%20🎁🐍&fontSize=42&fontColor=ffffff&fontAlignY=40&descAlignY=70" />
</p>


<p align="center">
  <img src="https://img.shields.io/badge/language-Python%203.12-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/AoC-2025-6f42c1" />
  <img src="https://img.shields.io/badge/status-in_progress-yellow" />
</p>

## ⭐ Progress ⭐

<p align="center">

| Day    | Status   | Time |
|:-------|:--------:|:----:|
| [Day 1 : Secret Entrance](https://adventofcode.com/2025/day/1)  |   ⭐⭐   |   1.192 ms   |

</p>

## 🚀 Run a Day 🚀

To execute Day **N**, run:

```bash
python3 main.py N
```

### Example

```bash
$ python3 main.py 7
--- Advent of Code — Day 07 ---
Part 1: 33
Part 2: 36
Time  : 0.769ms
```

## Summary

### Day 1

<details>
  <summary><strong>Show Day 1</strong></summary>

  **Status:**  
  ![Patata](https://img.shields.io/badge/Day%201-completed-BFFFD1)

  **Solution overview:**
  It's the first day, that means the solution is pretty straightforward. Part 1 is really easy so I will talk a bit about part 2 instead. The main issue with part 2 if you want to do it without brute-force the main problem is when the dial points at 0. You need to check what happens everytime the dial goes to 0, and the when the previous dial was 0. I ended checking every possibility and then merging the possibilities as follows:

```python
if new_pos > 0:
    sol2 += abs(new_pos // 100)
else:
    sol2 += abs((new_pos-1) // 100)
    if pos == 0:
        sol2 -= 1
```

</details>
