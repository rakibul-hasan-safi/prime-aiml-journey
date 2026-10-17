"""
Q4. Write a function to return the count of the number of digits in a number, n.
"""

n = input("Enter the number: ")

count = 0
for char in n:
    count += 1

print(count)

# Sample run:
# Enter the number: 12345
# 5
