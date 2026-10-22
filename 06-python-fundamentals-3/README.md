# 06 · Python Fundamentals (Part 3)

Strings, lists, tuples, dictionaries and sets: the five collection types that every dataset later in the course is built from.

## Lessons · 14 videos · 1 h 7 min

| # | Lesson | Length | # | Lesson | Length |
|---|--------|--------|---|--------|--------|
| 1 | Strings in Python | 05:22 | 8 | Tuple Methods | 02:17 |
| 2 | Slicing in Strings | 05:06 | 9 | Dictionary in Python | 04:27 |
| 3 | String Formatting – f-string & format() | 06:59 | 10 | Dictionary Methods | 04:49 |
| 4 | Lists in Python | 07:10 | 11 | Sets in Python | 03:25 |
| 5 | List Methods | 04:22 | 12 | Set Methods | 02:52 |
| 6 | Using Loops with Lists | 03:58 | 13 | Practice Problem (Part a & b) | 05:41 |
| 7 | Tuples in Python | 03:27 | 14 | Practice Problem (Part c) | 07:03 |

## Assignment 3

⏳ In progress. Solutions will go in `assignment-3/`.

## The 5 collections at a glance

|  | String | List | Tuple | Dict | Set |
|--|--------|------|-------|------|-----|
| Syntax | `"..."` | `[ ]` | `( )` | `{k: v}` | `{ }` / `set()` |
| Ordered | ✅ | ✅ | ✅ | ✅ (3.7+) | ❌ |
| Mutable | ❌ | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ✅ | keys: ❌ | ❌ |
| Indexing / slicing | ✅ | ✅ | ✅ | by key | ❌ |

**Choosing one:** look something up by name → dict · only unique values → set · data that must not change → tuple · anything else ordered → list.

## Key notes

**Slicing** `seq[start:stop:step]` works on strings, lists and tuples. `stop` is excluded.

```python
s = "Python"
s[0:2]    # 'Py'
s[-3:]    # 'hon'
s[::-1]   # 'nohtyP'
```

**f-strings** are the preferred way to format output:

```python
f"accuracy = {0.9134:.1%}"   # accuracy = 91.3%
f"{523.4000000000001:.1f}"   # 523.4
```

**List methods:** `append(x)`, `insert(i, x)`, `sort()`, `sort(reverse=True)`, `reverse()`, `remove(x)`, `pop()`.
`sort()`, `reverse()` and `append()` change the list in place and return `None`. `sorted(l)` returns a new list.

**Dict methods:** `keys()`, `values()`, `items()`, `get(k, default)`, `update({...})`.
`d["missing"]` raises a `KeyError`; `d.get("missing")` returns `None`.

**Set methods:** `add`, `remove` (error if missing), `discard` (silent), `pop`, `clear`, `union` / `|`, `intersection` / `&`, `difference` / `-`.

## Gotchas

- `{}` is an empty **dict**. An empty set is `set()`.
- A one-element tuple needs a comma: `(42,)`.
- `b = a` doesn't copy a list; use `a.copy()` or `a[:]`.
- Lists can't be dict keys or set items; tuples can.
- Avoid naming variables `list`, `dict`, `set`, `str` or `sum`, since that hides the built-ins.
