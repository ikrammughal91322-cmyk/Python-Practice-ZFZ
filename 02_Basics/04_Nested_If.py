age = int(input("Enter your age: "))
if age >=18:
    if age <=60:
        print("Eligible")
    else:
        print("Age Limit Exceeded")
else:
    print("Under age")


mark = int(input("Enter your marks"))
if mark >=40:
    if mark >= 80:
        print("Excellent")
    else:
        print("Pass")
else:
    print("Fail")