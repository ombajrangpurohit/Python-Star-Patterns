rows = 5
for i in range(rows):
    for j in range(i):
        print(" ", end = " ")
    for j in range(9 - (2 * i)):
        print("*", end = " ")
    print()