# Lesson: Loops (practice set 2)
# Sum of the first n natural numbers using a for loop and range()

n = int(input("Enter your number: "))

sum = 0
for i in range(1, n+1):
    sum += i

print("Sum = ", sum)

# Sample run:
# Enter your number: 10
# Sum =  55
