"""
Q3. Ask the user to enter two integers and one float. Convert them all to floats
and print their average.
"""

number1 = float(input("Enter the first integer: "))
number2 = float(input("Enter the second integer: "))
float_number = float(input("Enter a float number: "))

average = (number1 + number2 + float_number) /3;
print("The average of", number1, ",", number2, "and", float_number, "is", average)

# Sample run:
# Enter the first integer: 2
# Enter the second integer: 5
# Enter a float number: 7.5
# The average of 2.0 , 5.0 and 7.5 is 4.833333333333333
