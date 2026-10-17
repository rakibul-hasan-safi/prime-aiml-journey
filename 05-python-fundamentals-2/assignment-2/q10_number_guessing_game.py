"""
Q10. Create a "Number Guessing Game". Given a secret number (decided by you), ask the
user to guess it and print:
  - "Too high" if the guess is above the number
  - "Too low" if the guess is below
  - "Correct!" if the guess matches
"""

number = 15
guess = int(input("Guess the number: "))

if guess > number:
    print("Too High")
elif guess < number:
    print("Too Low")
elif guess == number:
    print("Correct")

# Sample run:
# Guess the number: 15
# Correct
#
# Guess the number: 18
# Too High
#
# Guess the number: 5
# Too Low
