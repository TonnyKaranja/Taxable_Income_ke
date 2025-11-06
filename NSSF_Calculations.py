
# Task 16: NHIF and NSSF Calculation Program (Kenya)

# Get inputs
basic_salary = float(input("basic salary: "))
benefits = float(input("total benefits: "))

# Calculate gross salary
gross_salary = basic_salary + benefits
print(f"Gross Salary: KSh {gross_salary:,.2f}")

# --- NHIF Calculation ---
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

# --- NSSF Calculation ---
# Use the minimum of gross salary and 18,000
nssf_base = min(gross_salary, 18000)
nssf = 0.06 * nssf_base

# --- Display results ---
print(f"NHIF Deduction: KSh {nhif:,.2f}")
print(f"NSSF Deduction: KSh {nssf:,.2f}")
