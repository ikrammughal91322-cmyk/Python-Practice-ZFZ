n = 9
m = 9
for i in range(n):
    for j in range(2 * n-1):
        if i == n-1 or j == n - i -1 or j == n + i -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()