"""
Q4. The user enters a string containing a number (e.g. "45"). Convert it to:
  - an integer
  - a float
  - a string again
Print all three values with their types.
"""

user_input = input ("Enter a number as a string: ")
# Convert to integer
integer_value = int(user_input)
# Convert to float
float_value = float(user_input)
# Convert back to string
string_value = str(user_input)
# Print the values and their types
print("Integer value:", integer_value, "Type: ", type(integer_value))
print("Float value:", float_value, "Type: ", type(float_value))
print("String value:", string_value, "Type: ", type(string_value))

# Sample run:
# Enter a number as a string: 45
# Integer value: 45 Type:  <class 'int'>
# Float value: 45.0 Type:  <class 'float'>
# String value: 45 Type:  <class 'str'>
