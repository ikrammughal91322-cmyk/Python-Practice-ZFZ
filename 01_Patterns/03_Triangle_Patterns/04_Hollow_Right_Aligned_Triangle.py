n = 9
m = 9
for i in range(n):
    for j in range(m):
        if j == m-1 or i == n-1 or i +j == m-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()