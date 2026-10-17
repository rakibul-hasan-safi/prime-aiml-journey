"""
Q1. Write a program that takes salary as input. Using conditional statements,
calculate the final tax rate based on these rules:
  - If salary < 30,000       -> 5%
  - If salary is 30,000-70,000 -> 15%
  - If salary > 70,000       -> 25%
"""

salary = float(input("Enter your Salary: "))

if salary < 30000:
    print("Final Tax Rate is 5%")
elif salary >= 30000 and salary <= 70000:
    print("Final Tax Rate is 15%")
else:
    print("Final Tax Rate is 25%")

# Sample runs:
# Enter your Salary: 25000
# Final Tax Rate is 5%
#
# Enter your Salary: 33000
# Final Tax Rate is 15%
#
# Enter your Salary: 100000
# Final Tax Rate is 25%

# Fix: the first version used `or`, which is True for every salary,
# so the 25% branch never ran. A range needs both conditions -> `and`.
