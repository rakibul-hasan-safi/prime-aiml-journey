"""
Q10. Take a decimal number as input (like 45.78) and output its:
  - integer part    -> 45
  - fractional part -> .78
"""

number = float(input("Enter a decimal number: "))
integer_part = int(number)
fractional_part = number - integer_part
print("Integer part:", integer_part)
print("Fractional part:", fractional_part)

# Sample run:
# Enter a decimal number: 21.56
# Integer part: 21
# Fractional part: 0.5599999999999987
