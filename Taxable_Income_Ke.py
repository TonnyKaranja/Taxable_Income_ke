
# Task 18: Calculate Taxable Income
# Author: Tonny Karanja
# Description: Computes NHIF, NSSF, NHDF, Gross Salary, and finally the Taxable Income

# Input
basic_salary = float(input("basic salary: "))
benefits = float(input("benefits: "))

# Gross salary
gross_salary = basic_salary + benefits

# ---------------------------
# NHIF Calculation (Kenya Rates)
# ---------------------------
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

nhif = calculate_nhif(gross_salary)

# ---------------------------
# NSSF Calculation (6% capped at 18,000)
# ---------------------------
nssf = 0.06 * min(gross_salary, 18000)

# ---------------------------
# NHDF Calculation (1.5% of Gross Salary)
# ---------------------------
nhdf = gross_salary * 0.015

# ---------------------------
# Taxable Income
# ---------------------------
taxable_income = gross_salary - (nhif + nssf + nhdf)

# ---------------------------
# Output Summary
# ---------------------------
print("\n--- SALARY SUMMARY ---")
print(f"Basic Salary: Ksh {basic_salary:,.2f}")
print(f"Benefits: Ksh {benefits:,.2f}")
print(f"Gross Salary: Ksh {gross_salary:,.2f}")
print(f"NHIF Deduction: Ksh {nhif:,.2f}")
print(f"NSSF Deduction: Ksh {nssf:,.2f}")
print(f"NHDF Deduction: Ksh {nhdf:,.2f}")
print(f"Taxable Income: Ksh {taxable_income:,.2f}")
