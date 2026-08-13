n = 9
m = 9
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*(n-i)-1):
        print("*",end=" ")
    print()