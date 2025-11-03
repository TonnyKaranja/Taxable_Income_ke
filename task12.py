
# Programming to find the largest of four numbers without using max()


num1 = float(input("first number: "))
num2 = float(input("second number: "))
num3 = float(input("third number: "))
num4 = float(input("fourth number: "))


largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4

print("The largest number is:", largest)
