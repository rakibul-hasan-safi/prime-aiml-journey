"""
Q6. Write a program to swap values of two numbers entered by the user.
"""

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

print("Before swapping: number1 =", number1, "number2 =", number2)

# Swap the values
temp = number1
number1 = number2
number2 = temp

print("After swapping: number1 =", number1, "number2 =", number2)

# Sample run:
# Enter the first number: 8
# Enter the second number: 4
# Before swapping: number1 = 8 number2 = 4
# After swapping: number1 = 4 number2 = 8
