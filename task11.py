
# Programming to calculate age in years, months, and days

from datetime import date

birth_year = int(input("birth year: "))
birth_month = int(input("birth month: "))
birth_day = int(input("birth day: "))


today = date.today()

dob = date(birth_year, birth_month, birth_day)


days_difference = (today - dob).days


years = days_difference // 365
months = (days_difference % 365) // 30
days = (days_difference % 365) % 30

print("Your age is:", years, "years,", months, "months and", days, "days old.")
