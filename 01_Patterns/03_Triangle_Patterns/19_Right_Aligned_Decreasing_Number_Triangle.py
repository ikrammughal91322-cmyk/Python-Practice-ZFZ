n = 5
m = 5
for i in range(n):
    num = 5
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(num,end=" ")
        num -= 1
    print()