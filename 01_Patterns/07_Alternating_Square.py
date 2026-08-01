for i in range(7):
    for j in range(7):
        if (i + j) % 2 == 0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()
        