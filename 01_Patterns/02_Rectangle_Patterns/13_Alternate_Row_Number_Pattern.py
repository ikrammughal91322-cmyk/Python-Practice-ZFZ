n = 7
m = 9
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print(j + 1,end=" ")
        else:
            print(m-j,end=" ")
    print()