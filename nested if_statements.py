
#take three inputs from a user, separately. print the largest of the numbers. Hint: Determine what type of data is taken in as input.
#all inputs are always strings
# Take three inputs from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Use nested if statements to find the largest number
if num1 >= num2:
    if num1 >= num3:
        print("The largest number is:", num1)
    else:
        print("The largest number is:", num3)
else:
    if num2 >= num3:
        print("The largest number is:", num2)
    else:
        print("The largest number is:", num3)


#take as input from user the temperature if the temperature is above 30 degrees c display "the temperature is too high" if the temperature is above 15 display "normal temperature" otherwise display  " cold temperature"
#data types, input() always gives a string

# Take temperature input from user
temperature = float(input("Enter the temperature in degrees Celsius: "))

# Check the temperature range
if temperature > 30:
    print("The temperature is too high")
elif temperature > 15:
    print("Normal temperature")
else:
    print("Cold temperature")

    #write a python program that checks if a variable x is between10 and 20 (inclusive) and if another variable y is greater than 100. if both conditions are true, print "conditions met", otherwise print "conditions not met"
    #Have two variables, x and y
    #x must be between 10 and 20 (inclusive) → meaning 10 ≤ x ≤ 20
    #y must be greater than 100
    #If both conditions are true → print "conditions met".
    #Otherwise → print "conditions not met".

    # Take input values for x and y
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

# Check both conditions using 'and'
if (x >= 10 and x <= 20) and (y > 100):
    print("Conditions met")
else:
    print("Conditions not met")


#write a python program that checks if a variable password is equal to the string "secret123". if it is, print "Access granted", otherwise print "Access denied"


# Ask the user to enter a password
password = input("Enter your password: ")

# Check if it matches 'secret123'
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

    #nested if

    # Take inputs from user
student_score = int(input("Enter student score: "))
attendance = int(input("Enter attendance percentage: "))

# Check conditions using nested if
if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")













