rows = 5
for i in range(rows):
    for j in range(rows):
        if  j >= rows - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()
# --- IGNORE ---
# End of recent edits
# i = 0, j = 0,1,2,3,4