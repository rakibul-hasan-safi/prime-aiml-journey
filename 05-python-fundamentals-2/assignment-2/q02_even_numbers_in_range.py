"""
Q2. Write a function that takes two integers a and b and prints all even
numbers between them (inclusive).
"""

numberA = int(input("Enter number a: "))
numberB = int(input("Enter number b: "))

for number in range(numberA, numberB+1):
    if (number % 2 == 0):
        print(number)

# Sample run:
# Enter number a: 5
# Enter number b: 15
# 6
# 8
# 10
# 12
# 14
