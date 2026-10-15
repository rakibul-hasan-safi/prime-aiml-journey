# 04 · Python Fundamentals (Part 1)

Output, variables, data types, operators, type casting, and user input. Everything needed to write a small program that takes input, computes something, and prints the result.

## Lesson code

| File | Topic | What it does |
|------|-------|--------------|
| [01_hello_world.py](./01_hello_world.py) | `print()` | First program |
| [02_variables.py](./02_variables.py) | Variables | Stores a name, age, and PI and prints them |
| [03_sum_of_two_numbers.py](./03_sum_of_two_numbers.py) | Arithmetic operators | Adds two numbers |
| [04_average_of_two_numbers.py](./04_average_of_two_numbers.py) | `input()` + casting | Averages two numbers typed by the user |

Run any file with:

```bash
python3 01_hello_world.py
```

## Assignment problems

| # | Problem | Status |
|---|---------|--------|
| Q1 | [Greet with name and age](./problems/q01_greet_name_age.py) | ⏳ |
| Q2 | [Sum, difference, product, quotient](./problems/q02_basic_calculator.py) | ⏳ |
| Q3 | [Average of two ints and a float](./problems/q03_average_of_three.py) | ⏳ |
| Q4 | [String to int, float, and back](./problems/q04_string_conversions.py) | ⏳ |

## Key notes

**Data types:** `int`, `float`, `str`, `bool`, `None`. Check with `type(x)`.

**Operators**

| Kind | Operators |
|------|-----------|
| Arithmetic | `+  -  *  /  //  %  **` |
| Relational | `==  !=  >  <  >=  <=` |
| Assignment | `=  +=  -=  *=  /=  %=  **=` |
| Logical | `and  or  not` |

- `/` always returns a float (`10 / 2` → `5.0`); `//` rounds down (`7 // 2` → `3`)
- Precedence: `()` → `**` → unary → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`
- `input()` always returns a **string**. Cast it: `int(input())` or `float(input())`
- `int("3.5")` raises a `ValueError`; use `float()` for decimals

## Lessons learned

- Python doesn't need semicolons. My early files have them (a Java habit), and they still run, but newer code drops them.
- `sum` is a built-in function, so a name like `total` is safer for a variable.
- Typed `pyton3` once and got `command not found`. Read the error literally; it's usually a typo.
