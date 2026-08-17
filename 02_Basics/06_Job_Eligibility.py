age = int(input("Enter your age: "))
education = int(input("1 = Bachelor's , 0 = Non Bachelor: "))
experience = int(input("Enter your experience: "))
if age >= 18:
    if education == 1:
        if experience >= 2:
            print("Eligible")
        else:
            print("Experience Required")
    else:
        print("Bachelor Required")
else:
    print("Under age")