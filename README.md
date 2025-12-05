<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=8A2BE2&text=Advent%20of%20Code%202025%20🎁🐍&fontSize=42&fontColor=ffffff&fontAlignY=40&descAlignY=70" />
</p>


<p align="center">
  <img src="https://img.shields.io/badge/language-Python%203.12-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/AoC-2025-6f42c1" />
  <img src="https://img.shields.io/badge/status-in_progress-yellow" />
</p>

## ⭐ Progress ⭐

| Day    | Status   | Time |
|:-------|:--------:|:----:|
| [Day 1 : Secret Entrance](https://adventofcode.com/2025/day/1)  |   ⭐⭐   |   1.192 ms   |
| [Day 2 : Gift Shop](https://adventofcode.com/2025/day/2)  |   ⭐⭐   |   1.355 ms   |
| [Day 3 : Lobby](https://adventofcode.com/2025/day/3)  |   ⭐⭐   |   8.343 ms   |
| [Day 4 : Printing Department](https://adventofcode.com/2025/day/4)  |   ⭐⭐   |   55.344 ms   |
| [Day 5 : Cafeteria](https://adventofcode.com/2025/day/5)  |   ⭐⭐   |   0.876 ms   |

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

## 📑 Summary 📑

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
  ![Patata](https://img.shields.io/badge/Day%202-completed-BFFFD1)

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

### Day 3

<details>
  <summary><strong>Show Day 3</strong></summary>

  **Status:**  
  ![Patata](https://img.shields.io/badge/Day%203-completed-BFFFD1)

  **Solution overview:**
  This was way easier than yesterday. You need to follow one simple rule to solve this problem. Get the highest number and continue to the next digit right after that number. You need to be careful to leave space for the rest of the digits but overall it was not very hard. Part 2 is as follows:

```python
def part2(data):
    sol2 = 0
    for seq in data:
        vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        i = -1
        for digit in range(11, -1, -1):
            for j in range(i+1,len(seq)-digit):
                if int(seq[j]) > vals[digit]:
                    vals[digit] = int(seq[j])
                    i = j
                if vals[digit] == 9:
                    break

        sol2 += sum([d * (10 ** i) for i, d in enumerate(vals)])
    
    return sol2
```

Part one is very similiar, the only difference is that the I don't loop over the 2 digits. Instead, I calculate them in the same loop.

</details>

### Day 4

<details>
  <summary><strong>Show Day 4</strong></summary>

  **Status:**  
  ![Patata](https://img.shields.io/badge/Day%204-completed-BFFFD1)

  **Solution overview:**
  If you are confident with 2 dimensional grids, this is by far the easiest problem so far. I decided to use sets and just check the cells where a paper roll was. Part 1 is really straigforward and in part 2 I used a queue and add the neightbour cells that change to the next queue until that queue is empty and then we exit the loop.

  I don't have a lot to say about the code, this day was really straightforward, so here is some paper rolls 🧻🧻🧻🧻🧻🧻.

</details>

### Day 5

<details>
  <summary><strong>Show Day 5</strong></summary>

  **Status:**  
  ![Patata](https://img.shields.io/badge/Day%205-completed-BFFFD1)

  **Solution overview:**
  Ok, this one might be the hardest up to now. But it isn't really that hard if you have programmed an union interval algorithm before.

  First, I did the part 1 as someone would expect but I noticed that it could be done with binary search. You can sort the intervals by the left part of the interval and then compute binary search to look if the id is in... Wait, it gave me a wrong answer... I get it, that's because some intervals are way bigger than others and interval things like $b \subseteq c$ where $b$ and $c$ are intervals can happen and the algorithm would look interval $b$ but not $c$. But this would be possible if the intersection of all the intervals were $\emptyset$. And part 2 may ask us to find that set.

  So I basically solved part 2 and found the union of the sets, so the new every interval intersection in the new set is $\emptyset$, and then I made the binary search as follows:

  ```python
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
  ```

  I'm quite happy with how fast I found this. Union algorithm basically consist in picking an interval and then finding the intervals which intersection is non-empty and making a new interval until none of the intervals intersects with it, then you continue with the next interval.

  This one is the fastest solution this year so far clocking under 1ms.

</details>
