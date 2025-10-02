row_1 = 5
row_2 = 4
for i in range(row_1):
    for j in range(row_1 -  i - 1):
        print(" ", end=" ")
    for j in range( i + 1):
        print("*", end=" ")
    print()
for i in range(row_2):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(row_2 - i):
        print("*", end=" ")
    print()