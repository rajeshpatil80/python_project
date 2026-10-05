rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == 1 or i == rows or j == 1 or j == rows:  # Print numbers only on borders
            print(j, end=" ")
        else:
            print(" ", end=" ")  # Print space inside
    print()  # Move to the next line

    # /*output
    # Enter the row size for the pattern: 4
    # 1 2 3 4
    # 1     4
    # 1     4
    # 1 2 3 4
    # */