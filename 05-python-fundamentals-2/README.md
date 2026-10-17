# 05 · Python Fundamentals (Part 2)

Conditionals, loops, and functions: the tools that let a program make decisions, repeat work, and reuse logic.

## Lesson code

| File | Topic | What it does |
|------|-------|--------------|
| [01_sum_of_n_natural_numbers.py](./01_sum_of_n_natural_numbers.py) | `for` + `range()` | Adds 1 through n |

## Assignment 2 · 10 solved · 2 need a fix

| # | Problem | Concept | Status |
|---|---------|---------|--------|
| Q1 | [Tax rate by salary](./assignment-2/q01_tax_rate.py) | `if` / `elif` / `else` | ⚠️ Fix: `or` → `and` |
| Q2 | [Even numbers between a and b](./assignment-2/q02_even_numbers_in_range.py) | `for` + `range()` | ✅ |
| Q3 | [Print the digits of n](./assignment-2/q03_print_digits.py) | `%` and `//` in a `while` loop | ✅ |
| Q4 | [Count digits](./assignment-2/q04_count_digits.py) | Looping over a string | ✅ |
| Q5 | [Sum of digits](./assignment-2/q05_sum_of_digits.py) | `while` loop | ✅ |
| Q6 | [1–100 divisible by 3 and 5](./assignment-2/q06_divisible_by_3_and_5.py) | `and` in a condition | ✅ |
| Q7 | [Positive or negative until "Quit"](./assignment-2/q07_positive_negative_until_quit.py) | `while True` + `break` | ⚠️ Fix: `continue` → `break` |
| Q8 | [Simple calculator](./assignment-2/q08_simple_calculator.py) | `if` / `elif` chain | ✅ |
| Q9 | [Prime check](./assignment-2/q09_prime_check.py) | Loop + `break` + flag variable | ✅ |
| Q10 | [Number guessing game](./assignment-2/q10_number_guessing_game.py) | Comparisons | ✅ |

### The two fixes

**Q1:** `salary >= 30000 or salary <= 70000` is true for every salary, so anyone earning over 70,000 is still told 15% and the 25% branch never runs. A range needs both conditions:

```python
elif salary >= 30000 and salary <= 70000:
```

**Q7:** `continue` jumps back to the start of the loop, so the program never ends. Typing `Quit` (capital Q, as the question says) also crashes on `int("Quit")`. `break` exits the loop:

```python
if n == "Quit" or n == "quit":
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
