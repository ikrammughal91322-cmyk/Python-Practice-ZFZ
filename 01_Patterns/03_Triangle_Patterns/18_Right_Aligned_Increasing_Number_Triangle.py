n = 10
m = 10
for i in range(n):
    num = 1
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(num,end=" ")
        num +=1
    print()