"""
Q5. Write a function to return the sum of digits of a number, n.
"""

n = int(input("Enter the number: "))

sum = 0

while n > 0:
    sum = sum + n % 10
    n = n//10

print(sum)

# Sample run:
# Enter the number: 12345
# 15
