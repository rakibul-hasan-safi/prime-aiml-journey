"""
Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3
and 5.
"""

n = 1

while n <= 100:
    if (n % 3 == 0 and n % 5 == 0):
        print(n)
    n = n+1

# Sample run:
# 15
# 30
# 45
# 60
# 75
# 90
