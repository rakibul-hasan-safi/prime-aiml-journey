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

## Assignment 1 · 10/10 solved ✅

| # | Problem | Concept |
|---|---------|---------|
| Q1 | [Greet with name and age](./assignment-1/q01_greet_name_age.py) | `input()`, `int()` |
| Q2 | [Sum, difference, product, quotient](./assignment-1/q02_basic_calculator.py) | Arithmetic operators |
| Q3 | [Average of two ints and a float](./assignment-1/q03_average_of_three.py) | Casting to `float` |
| Q4 | [String to int, float, and back](./assignment-1/q04_string_conversions.py) | `int()`, `float()`, `str()`, `type()` |
| Q5 | [Evaluate `10 + 3 * 2 ** 2`](./assignment-1/q05_operator_precedence.py) | Operator precedence |
| Q6 | [Swap two numbers](./assignment-1/q06_swap_two_numbers.py) | Temp variable |
| Q7 | [Celsius to Fahrenheit](./assignment-1/q07_celsius_to_fahrenheit.py) | Formulas with floats |
| Q8 | [Area of a circle](./assignment-1/q08_area_of_circle.py) | `**` power |
| Q9 | [Simple interest](./assignment-1/q09_simple_interest.py) | Multi-input math |
| Q10 | [Integer and fractional part](./assignment-1/q10_integer_and_fractional_part.py) | `int()` truncation |

Each file has the question at the top, my solution, and a sample run.

### Things to improve later

- **Q1:** commas in `print()` add spaces, so the output is `Hello Safi ! You are 23 years old` rather than `Hello Safi, you are 23 years old!`. F-strings, coming later, fix this: `print(f"Hello {name}, you are {age} years old!")`.
- **Q2:** label each result (`print("Sum:", ...)`) so the output is easy to read.
- **Q6:** Python can swap in one line: `a, b = b, a`.
- **Q7 and Q10:** outputs like `523.4000000000001` and `0.5599999999999987` come from how computers store decimals. `round(x, 2)` cleans them up.

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
