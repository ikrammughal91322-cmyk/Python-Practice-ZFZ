n = 9
m = 9
for i in range(n):
    num = 1
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print(num,end=" ")
        num += 1
    print()