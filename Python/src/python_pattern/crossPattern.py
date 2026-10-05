rows = int(input("Enter the row size for the pattern: "))  # Ask for the pattern size and convert the user's input to an integer.

for i in range(1, rows + 1):  # Loop through each row, numbering them from 1 to rows.
    for j in range(1, rows + 1):  # Loop through each column in the current row.
        if i == j or i + j == rows + 1:  # Check whether this position is on either diagonal of the pattern.
            print("*", end=" ")  # Print a star on a diagonal and stay on the same line.
        else:  # Run this when the position is not on either diagonal.
            print(" ", end=" ")  # Print a blank space to keep the pattern aligned.
    print()  # Finish the current row and move to the next line.

# Example output when the user enters 5:
# *       *
#   *   *
#     *
#   *   *
# *       *