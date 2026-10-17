"""
Q8. Create a Simple Calculator that performs arithmetic operations. Create a function
calculator(a, b, operation) that performs addition, subtraction, multiplication,
or division based on the operation parameter ('+', '-', '*' or '/').
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Choose your operation + , - , * , / : ")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Wrong Operation")

# Sample run:
# Enter first number: 2
# Enter second number: 5
# Choose your operation + , - , * , / : *
# 10
