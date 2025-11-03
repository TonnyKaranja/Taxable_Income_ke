
# Program validating and formating a phone number

# enter a phone number in terminal

phone = input("phone number: ")

# Removing any spaces in case its added
phone = phone.strip()

# Check and convert based on how it starts
if phone.startswith("+254"):
    formatted = phone
elif phone.startswith("07"):
    formatted = "+254" + phone[1:]
elif phone.startswith("7"):
    formatted = "+254" + phone
elif phone.startswith("254"):
    formatted = "+" + phone
elif phone.startswith("01"):
    formatted = "+254" + phone[1:]
elif phone.startswith("1"):
    formatted = "+254" + phone
else:
    formatted = "Invalid phone number format!"

# Displaying the formatted number
print("Formatted phone number:", formatted)
