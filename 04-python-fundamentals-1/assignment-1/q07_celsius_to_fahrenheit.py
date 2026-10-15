"""
Q7. Ask the user for a temperature in Celsius (string input). Convert it to float,
then calculate and print the temperature in Fahrenheit.

    Fahrenheit = (Celsius * (9/5)) + 32
"""

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * (9/5)) + 32
print("The temperature in Fahrenheit is:", fahrenheit)

# Sample run:
# Enter the temperature in Celsius: 273
# The temperature in Fahrenheit is: 523.4000000000001
