
# spa_service.py
# Conditional statements example — Rayne Spa

# Ask the user for their preferred service
service = input("Welcome to Rayne Spa!What service would you like today? (waxing / massage / facial): ").lower()

# Check the service and respond accordingly
if service == "waxing":
    print("Prepare waxing kit")
elif service == "massage":
    print("Prepare massage oils")
elif service == "facial":
    print("Prepare facial steamer and towels")
else:
    print("Sorry, that service is not available today")

print("Thank you for choosing Rayne Spa")
