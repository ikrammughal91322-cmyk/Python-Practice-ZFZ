n = 19
m = 19
for i in range(n):
    for j in range(m):
        if i == n-1 or i+j == m-1 or j == m-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()