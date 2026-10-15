"""
Q5. Evaluate and print the result of the following expression:

    x = 10 + 3 * 2 ** 2

Based on what you learnt in the lecture, explain why the output is what it is.
"""

x = 10 + 3 * 2 ** 2
print(x)
# The expression `x = 10 + 3 * 2 ** 2` follows the order of operations, also known as PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction). According to this rule, we first evaluate the exponentiation, then perform the multiplication, and finally the addition.
# 1. First, we calculate the exponentiation: `2 ** 2` which equals `4`.
# 2. Next, we perform the multiplication: `3 * 4` which equals `12`.
# 3. Finally, we perform the addition: `10 + 12` which equals `22`.

# Sample run:
# 22
