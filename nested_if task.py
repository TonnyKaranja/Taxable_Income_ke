
from datetime import date

# Define the dates
start_date = date(2024, 1, 1)
end_date   = date(2024, 12, 31)

# Compare the dates
if start_date < end_date:
    print("Valid period")
elif start_date > end_date:
    print("Invalid period")
else:
    print("One-day period")


    # Define the list and variable first
valid_ids = [101, 102, 103]
user_id = 105

# Then check if user_id is in the list
if user_id in valid_ids:
    print("Access granted")
else:
    print("Access denied")


    value = 25  # you can change this to test different types

if isinstance(value, str):
    print("String detected")
elif isinstance(value, int):
    print("Integer detected")
else:
    print("Unknown type")


x = 7
y = 14

if x % 2 == 0:
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("only x is even")
else:
    if y % 2 == 0:
        print("only y is even")
    else:
        print("neither x nor y are even")




    


