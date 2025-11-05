
#task 1 using funtions

def triangle_area():
    base = float(input("base of the triangle: "))
    height = float(input("height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)


# Call the function
triangle_area()


#task 2 using functions

def check_number():
    number = int(input("a number: "))

    if number % 4 == 0:
        print("divisible by 4")
    elif number % 2 == 0:
        print("even")
    else:
        print("odd")

# Call the function
check_number()




#task on slide 70
#Create:
#A function to calculate total
#A function to calculate average
#A function to find the grade using the average


def get_total(maths, eng, swa, sci, sos):
    total = maths + eng + swa + sci + sos
    return total

def get_average(total):
    average = total / 5
    return average

def get_grade(average):
    if average > 79:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "E"

maths = float(input("marks for Maths: "))
eng = float(input("marks for English: "))
swa = float(input("marks for Swahili: "))
sci = float(input("marks for Science: "))
sos = float(input("marks for Social Studies: "))

total = get_total(maths, eng, swa, sci, sos)
average = get_average(total)
grade = get_grade(average)

print("\n------ RESULTS ------")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
