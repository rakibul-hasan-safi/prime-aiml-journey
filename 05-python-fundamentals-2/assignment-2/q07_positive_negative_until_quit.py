"""
Q7. Design a program to continuously input a number n from the user and print if it is
positive or negative until the user enters "Quit".
"""

while True:
    n = (input("Enter the number: "))
    if n == "Quit" or n == "quit":
        print("Goodbye!")
        break
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
# Enter the number: Quit
# Goodbye!

# Fix: the first version used `continue`, which jumps back to the top of the
# loop, so the program never ended. Typing "Quit" also crashed on int("Quit").
# `break` exits the loop, and both spellings are now accepted.
