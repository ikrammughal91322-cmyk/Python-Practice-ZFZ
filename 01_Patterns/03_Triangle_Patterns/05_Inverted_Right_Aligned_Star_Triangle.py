n = 19
m = 19
for i in range(n):
    for j in range(i):
        print(" ",end="  ")
    for j in range(n-i):
        print("*",end="  ")
    print()