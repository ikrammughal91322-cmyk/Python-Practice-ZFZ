n = 9
m = 9
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(m-i):
        print(i+j+1,end=" ")
    print()