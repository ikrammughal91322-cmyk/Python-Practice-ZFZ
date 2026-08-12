n = 19
m = 19
for i in range (n):
    for j in range(m):
        if i == n-1 or j == 0 or i == j:
            print("*",end="")
        else:
            print(" ",end="")
    print() 