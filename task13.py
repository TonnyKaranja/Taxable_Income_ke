
# Programming to check login with only 3 attempts

# login details
correct_email = "admin@mail.com"
correct_password = "Admin@123"
attempts = 3

while attempts > 0:
    email = input("email: ")
    password = input("password: ")

    if email == correct_email and password == correct_password:
        print("Login is Successful")
        break
    else:
        attempts -= 1
        print("Invalid username or password! You have", attempts, "attempt(s) left.")

if attempts == 0:
    print("You have been blocked")
