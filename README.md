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
| [Day 2 : Gift Shop](https://adventofcode.com/2025/day/2)  |   ⭐⭐   |   1.355 ms   |

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

### Day 2

<details>
  <summary><strong>Show Day 2</strong></summary>

  **Status:**  
  ![Patata](https://img.shields.io/badge/Day%201-completed-BFFFD1)

  **Solution overview:**
  This got harder very quickly. I thought about doing bruteforce but I was sure part 2 was going to be this kind of problem where bruteforce is impossible. I was very wrong 🙃🙃🙃. So, what I made for part 1 is just checking the left half of the even-digit numbers inside the intervals and check if they fit the intervals. So, if I want to check the numbers from 1234 to 6789, I will check the numbers 12 to 67 and check if the repetitions (i.e. 1212, 1313, 1414...) are inside the interval.

```python
        for id in range(int(nx[0:len(nx)//2]), int(ny[0:len(ny)//2])+1):
            if int(p.x) <= int(str(id)+str(id)) and int(str(id)+str(id)) <= int(p.y):
                invalid_ids.append(int(str(id)+str(id)))
```

I also ignored all the odd-digit digit numbers and as the interval digit number difference is 1 you can start from a power of 10 if the smaller number is odd-digit or end at 999... if the bigger is odd-digit.

```python
        if len(p.x) == len(p.y) and len(p.x) % 2 == 0:
            nx, ny = p.x, p.y
        elif len(p.x) != len(p.y): # So the len of p.x is len(p.y)-1
            if len(p.x) % 2 == 0:
                nx, ny = p.x, '9'*len(p.x)
            else:
                nx, ny = '1' + '0'*(len(p.y)-1), p.y
        else:
            continue
```

For part 2 we can reuse the code from part2 but dividing the number in n equal parts from n=2 to n=len(number)/2, but in the end the only way to be a repetition is that the number of digits in the repetition is a divisor of the number of digits of the number, i.e. If a number has 6 digits, the only repetitions of the number must be 1-digit, 2-digit or 3-digit numbers. So we calculate the divisors of the digits of each part of the interval and then we do the same as in part 1:

```python
        divisors_check = set()
        divisors_check = set(divisors(len(nx)) + divisors(len(ny)))
        divisors_check.discard(1)
        
        for n in divisors_check:
            for id in range(inte(nx[0:math.floor(len(nx)/n)]), inte(ny[0:math.ceil(len(ny)/n)])+1):
                if int(p.x) <= int(str(id)*n) and int(str(id)*n) <= int(p.y):
                    invalid_ids.append(int(str(id)*n))
```

</details>
