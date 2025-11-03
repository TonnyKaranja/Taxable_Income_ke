
# Programing to find the largest of three numbers without using max()


num1 = float(input("first number: "))
num2 = float(input("second number: "))
num3 = float(input("third number: "))

# Comparing the numbers
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)
