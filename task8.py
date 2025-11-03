
# Programming to calculate demerit points based on car speed

speed = int(input("speed of the car (km/h): "))

if speed < 70:
    print("Ok")
else:
    extra_speed = speed - 70
    
    points = extra_speed // 5 

    print("Points:", points)

    if points > 12:
        print("License suspended")
