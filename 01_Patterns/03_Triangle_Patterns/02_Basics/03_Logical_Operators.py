age = int(input("Enter your age: "))
if age >=18 and age<=60:
    print("Eligible")
else:
    print("Not Eligible")



age = int(input("Enter your age: "))
if age < 18 or age >60:
    print("Not Eligible")
else:
    print("Eligible")


num = int(input("Enter the number: "))
if (10<= num and num<=50) and num % 2 ==0 :
    print("Vlid even number")
else:
    print("Not valid")



num = int(input("Enter the number: "))
if (num>=1 and num<= 100) and num % 5 == 0:
    print("valid")
else:
    print("Not Valid")


mark = int(input("Enter the marks: "))
if mark >= 90:
    print("Excellent")
elif mark < 40:
    print("Fail")
else:
    print("Average")



age = int(input("Enter your AGE: "))
if age < 13 or age > 60:
    print("Special Category")
else:
    print("Normal Category")



age = int(input("Enter your age"))
if not age >= 18:
    print("Minor")
else:
    print("Adult")



num = int(input("Enter the num: "))
if not (num>=10 and num <=50):
    print("Invalid Range")
else:
    print("Valid Range")


marks = int(input("Enter stu marks"))
Attendence = int(input("Enter stu Attendence"))
if marks >= 50 and Attendence >= 75:
    print("Eligible")
else:
    print("Not Eligible")


Marks = int(input("Enter marks: "))
ATTENDENCE = int(input("Enter attendence"))
if (Marks >= 80 and ATTENDENCE >=75) or Marks >= 90:
    print("Eligible")
else:
    print("Not Eligible")



age = int(input("Enter your age: "))
experience = int(input("Enter your experience: "))
if (age >= 18 and experience >=2) or experience >= 5:
    print("Eligible")
else:
    print("Not Eligible")