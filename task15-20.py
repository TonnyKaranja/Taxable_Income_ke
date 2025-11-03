
# Programming to calculate Gross Salary and NHIF deduction

basic_salary = float(input("basic salary: "))
benefits = float(input("benefits: "))

#Gross Salary
gross_salary = basic_salary + benefits
print("Gross Salary:", gross_salary)


#NHIF deduction
if gross_salary <= 159999:
    nhif = 1500
elif gross_salary <= 79999:
    nhif = 3000
elif gross_salary <= 119999:
    nhif = 4000
elif gross_salary <= 149999:
    nhif = 5000
elif gross_salary <= 199999:
    nhif = 6000
elif gross_salary <= 249999:
    nhif = 7500
elif gross_salary <= 299999:
    nhif = 8500
elif gross_salary <= 349999:
    nhif = 9000
elif gross_salary <= 399999:
    nhif = 9500
elif gross_salary <= 449999:
    nhif = 10000
else:
    nhif = 12000

print("Your NHIF Deduction is:", nhif)
