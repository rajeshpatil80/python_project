rows = int(input("Enter the row size for the pattern: "))  # Ask for the number of rows and convert the input to an integer.

for i in range(1, rows + 1):  # Build the upper half of the diamond, including its widest row.
    for j in range(rows - i):  # Add leading spaces so each row is centered.
        print(" ", end=" ")  # Print a space without moving to the next line.
    for k in range(1, i + 1):  # Count upward from A to the middle letter of this row.
        print(chr(64 + k), end=" ")  # Convert the number to a letter and print it.
    for l in range(i - 1, 0, -1):  # Count downward to create the descending letters.
        print(chr(64 + l), end=" ")  # Convert the number to a letter and print it.
    print()  # Move to the next line after finishing this row.

for i in range(rows - 1, 0, -1):  # Build the lower half, starting just below the widest row.
    for j in range(rows - i):  # Add leading spaces to keep this row centered.
        print(" ", end=" ")  # Print a space without moving to the next line.
    for k in range(1, i + 1):  # Count upward from A to the middle letter of this row.
        print(chr(64 + k), end=" ")  # Convert the number to a letter and print it.
    for l in range(i - 1, 0, -1):  # Count downward to complete the row's letter pattern.
        print(chr(64 + l), end=" ")  # Convert the number to a letter and print it.
    print()  # Move to the next line after finishing this row.