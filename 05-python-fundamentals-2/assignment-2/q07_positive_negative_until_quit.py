"""
Q7. Design a program to continuously input a number n from the user and print if it is
positive or negative until the user enters "Quit".
"""

while True:
    n = (input("Enter the number: "))
    if n == "quit":
        print("Lets start again")
        continue
    number = int(n)
    if number < 0:
        print("The number is Negative")
    else:
        print("The number is Positive")

# Sample run:
# Enter the number: -2
# The number is Negative
# Enter the number: 20
# The number is Positive
# Enter the number: quit
# Lets start again
# Enter the number:
