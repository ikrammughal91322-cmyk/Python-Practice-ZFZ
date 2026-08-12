n = 19
m = 19
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or i+j == m:
            print("*",end="")
        else:
            print(" ",end="")
    print()
