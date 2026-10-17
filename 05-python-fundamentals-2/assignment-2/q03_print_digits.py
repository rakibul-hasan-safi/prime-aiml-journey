"""
Q3. Write a function that prints the digits of a number, n.
For example: n = 312 has 3 digits (3, 1 and 2) and we need to print them.

Hint: the right-most digit of N is N % 10, and N // 10 removes it.
"""

number = int(input("Enter the number: "))

while number > 0:
    print(number % 10)
    number = number//10

# Sample run:
# Enter the number: 123
# 3
# 2
# 1
