rows = int(input("Enter the row size for the pattern: "))  # Ask how many rows to print and convert the input to an integer.

for i in range(1, rows + 1):  # Process each row, starting at 1 and ending at the number entered.
    for j in range(rows - i):  # Calculate how many spaces to print before the stars on this row.
        print(" ", end=" ")  # Print a space without moving to the next line.
    for k in range(1, 2 * i):  # Print an odd number of stars, increasing by two on each row.
        print("*", end=" ")  # Print a star without moving to the next line.
    print()  # Finish the row and move to the next line.