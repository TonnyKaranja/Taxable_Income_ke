
# Programing to check password with only 4 attempts

# Correct password
correct_password = "admin@123"

attempts = 4

while attempts > 0:
    password = input("password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Wrong password! You have", attempts, "attempts left.")

if attempts == 0:
    print("Account blocked")
