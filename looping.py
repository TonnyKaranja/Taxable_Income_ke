
numbers = list(range(1, 51))
print(numbers)

numbers = list(range(1, 51))
divisible = []

for num in numbers:
    if num % 7 == 0 or num % 5 == 0:
        divisible.append(num)

print(divisible)

numbers = list(range(10, 41))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)



odd_numbers = []

for num in range(10, 51):
    if num % 2 != 0:
        odd_numbers.append(num)
        if len(odd_numbers) == 10:
            break

print(odd_numbers)



# Ask the user for a number
number = int(input("Enter a number: "))

# Use a for loop to print the multiplication table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


    count = 0

for num in range(1, 51):
    if num % 2 == 0:
        count += 1

print("Number of even numbers between 1 and 50:", count)



ls1 = [("Jay", "20"), ("Mo", "30"), ("Mya", "32")]

total = 0
for name, qty in ls1:
    total += int(qty)

print("Total quantity:", total)



