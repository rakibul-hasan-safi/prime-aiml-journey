"""
Q9. Write a function is_prime(n) that returns True if n is a prime number and
False otherwise, using a loop.

Hint: only numbers >= 2 can be prime. A non-prime n is divisible by at least one
number in the range [2, n-1].
"""

n = int(input("Enter your number: "))

i = 2
isPrime = True
while i < n:
    if n % i == 0:
        isPrime = False
        break
    i += 1
if isPrime and n > 1:
    print("The Number is Prime")
else:
    print("The Number is not Prime")

# Sample run:
# Enter your number: 9
# The Number is not Prime
