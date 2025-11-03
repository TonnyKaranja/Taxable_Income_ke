
# Program to check if a number is even or odd

number = int(input("a number: "))

# Checking if number is even or odd
if number % 2 == 0:
    print("even")
else:
    print("odd")

# Extra part: checking if it is divisible by 4
if number % 4 == 0:
    print("divisible by 4")
