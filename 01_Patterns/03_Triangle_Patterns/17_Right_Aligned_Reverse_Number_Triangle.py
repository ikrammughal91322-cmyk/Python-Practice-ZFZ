n = 9
m = 9
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(i-j+1,end=" ")
    print()