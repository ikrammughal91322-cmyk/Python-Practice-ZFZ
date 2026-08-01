m = 7
n = 7
for i in range(m):
    for j in range(n):
        if (i == 0 or i == m-1 or j == 0 or j == n-1):
            print("A", end=" ")
        elif(i == 1 or i == m-2 or j == 1 or j == n-2):
            print("B", end=" ")
        elif(i == 2 or i == m-3 or j == 2 or j == n-3):
            print("C", end=" ")
        else:
            print("D", end=" ")
    print()