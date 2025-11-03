
# Program to validate an email

# enter an email
email = input("my email: ")

# Removes any extra spaces
email = email.strip()

# Check if it contains "@" and "."
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
