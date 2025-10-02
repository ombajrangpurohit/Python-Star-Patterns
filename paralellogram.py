rows = 5
cols = 10
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for j in range(cols):
        print("*", end=" ")
    print()