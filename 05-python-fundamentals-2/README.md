# 05 · Python Fundamentals (Part 2)

Conditionals, loops, and functions: the tools that let a program make decisions, repeat work, and reuse logic.

## Lessons · 18 videos · 1 h 38 min

| # | Lesson | Length | # | Lesson | Length |
|---|--------|--------|---|--------|--------|
| 1 | Conditional Statements in Python | 08:05 | 10 | Loops using for | 09:22 |
| 2 | Practice Examples (Conditionals) | 09:02 | 11 | Vowel Count | 02:21 |
| 3 | Odd or Even | 01:55 | 12 | range() Function | 03:37 |
| 4 | Nesting | 04:38 | 13 | Sum of N numbers | 03:53 |
| 5 | Match case in Python | 03:56 | 14 | Functions in Python | 08:51 |
| 6 | Loops using while | 10:32 | 15 | Practice Examples (Functions) | 04:26 |
| 7 | Practice Examples (Loops) | 04:50 | 16 | Types of Functions | 01:49 |
| 8 | Multiplication Table of N | 04:37 | 17 | Lambda Functions | 03:27 |
| 9 | Break & Continue | 07:41 | 18 | Factorial of N | 05:10 |

## Lesson code

| File | Topic | What it does |
|------|-------|--------------|
| [01_sum_of_n_natural_numbers.py](./01_sum_of_n_natural_numbers.py) | `for` + `range()` | Adds 1 through n |

## Assignment 2 · 10/10 solved ✅

| # | Problem | Concept | Status |
|---|---------|---------|--------|
| Q1 | [Tax rate by salary](./assignment-2/q01_tax_rate.py) | `if` / `elif` / `else` | ✅ Fixed |
| Q2 | [Even numbers between a and b](./assignment-2/q02_even_numbers_in_range.py) | `for` + `range()` | ✅ |
| Q3 | [Print the digits of n](./assignment-2/q03_print_digits.py) | `%` and `//` in a `while` loop | ✅ |
| Q4 | [Count digits](./assignment-2/q04_count_digits.py) | Looping over a string | ✅ |
| Q5 | [Sum of digits](./assignment-2/q05_sum_of_digits.py) | `while` loop | ✅ |
| Q6 | [1–100 divisible by 3 and 5](./assignment-2/q06_divisible_by_3_and_5.py) | `and` in a condition | ✅ |
| Q7 | [Positive or negative until "Quit"](./assignment-2/q07_positive_negative_until_quit.py) | `while True` + `break` | ✅ Fixed |
| Q8 | [Simple calculator](./assignment-2/q08_simple_calculator.py) | `if` / `elif` chain | ✅ |
| Q9 | [Prime check](./assignment-2/q09_prime_check.py) | Loop + `break` + flag variable | ✅ |
| Q10 | [Number guessing game](./assignment-2/q10_number_guessing_game.py) | Comparisons | ✅ |

### Bugs found and fixed

**Q1:** the first version used `salary >= 30000 or salary <= 70000`, which is true for every salary, so anyone over 70,000 was told 15% and the 25% branch never ran. A range needs both conditions:

```python
elif salary >= 30000 and salary <= 70000:
```

Tested at 25,000 → 5%, 30,000 and 70,000 → 15%, 70,001 and 100,000 → 25%.

**Q7:** the first version used `continue`, which jumps back to the top of the loop, so the program never ended, and typing `Quit` crashed on `int("Quit")`. `break` exits the loop:

```python
if n == "Quit" or n == "quit":
    print("Goodbye!")
    break
```

### Next step for this set

Q2, Q3, Q4, Q5, Q8 and Q9 ask for a **function**, and Q4 and Q5 say *return*. These solutions get the right answers as plain scripts. Rewriting them with `def` and `return` (for example `def is_prime(n): ... return True`) is the part this chapter is practising.

## Key notes

- `if` → `elif` → `else`: only the **first** true branch runs
- `while` needs a start value, a condition, and an update, or it loops forever (stop it with Ctrl + C)
- `break` exits the loop; `continue` skips to the next round
- `range(start, stop, step)`: stop is **excluded**, so use `n + 1` to include n
- `return` hands a value back; `print` only shows it. A function with no `return` gives back `None`
- Don't name variables `sum`, `max`, or `input`; that hides Python's built-in functions
- `lambda x: x * x` is a one-line function
