"""
Q9. Ask the user for Principal (P), Rate (R), and Time (T). Convert all to float
and compute simple interest:

    SI = (P * R * T) / 100
"""

principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the rate of interest (R): "))
time = float(input("Enter the time in years (T): "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)

# Sample run:
# Enter the principal amount (P): 122
# Enter the rate of interest (R): 5
# Enter the time in years (T): 5
# The simple interest is: 30.5
