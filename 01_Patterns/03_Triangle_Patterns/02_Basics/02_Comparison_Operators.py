a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
result = a>b
print(type(result))
print(b<a)
print(a!=b)
print(a==b)
print(a<=c)
print(b>=c)


age = int(input("Enter your age:"))
if age >=18:
    print("You are eligible")
else:
    print("Sorry you are not eligible")