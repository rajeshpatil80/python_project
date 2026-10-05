rows = int(input("Enter the row size for the pattern: "))  # Ask how many rows to print, then convert the input to an integer.

for i in range(1, rows + 1):  # Process each row, starting at 1 and ending at the requested row count.
    for j in range(1, i + 1):  # Print as many letters on this row as its row number.
        print(chr(64 + j), end=" ")  # Convert 1 to A, 2 to B, and so on; print without starting a new line.
    print()  # Finish the current row and move to the next line.