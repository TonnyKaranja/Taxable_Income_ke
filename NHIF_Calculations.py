
#TASK 15: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that takes input of someone's basic salary and benefits,
#  adds them to find the gross salary then uses  the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using 

# Task 15: NHIF Calculation Program

# Get inputs
basic_salary = float(input("basic salary: "))
benefits = float(input("total benefits: "))

# Calculate gross salary
gross_salary = basic_salary + benefits
print(f"Gross Salary: KSh {gross_salary:,.2f}")

# Function to calculate NHIF based on gross salary
def calculate_nhif(gross):
    if gross <= 5999:
        return 150
    elif gross <= 7999:
        return 300
    elif gross <= 11999:
        return 400
    elif gross <= 14999:
        return 500
    elif gross <= 19999:
        return 600
    elif gross <= 24999:
        return 750
    elif gross <= 29999:
        return 850
    elif gross <= 34999:
        return 900
    elif gross <= 39999:
        return 950
    elif gross <= 44999:
        return 1000
    elif gross <= 49999:
        return 1100
    elif gross <= 59999:
        return 1200
    elif gross <= 69999:
        return 1300
    elif gross <= 79999:
        return 1400
    elif gross <= 89999:
        return 1500
    elif gross <= 99999:
        return 1600
    else:
        return 1700

# Calculate NHIF
nhif = calculate_nhif(gross_salary)

print(f"NHIF Deduction: KSh {nhif:,.2f}")

