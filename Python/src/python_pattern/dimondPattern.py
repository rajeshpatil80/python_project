rows = int(input("Enter the row size for the pattern: "))  # Ask for the number of rows and convert the input to an integer.

for i in range(1, rows + 1):  # Build the upper half, increasing the number of stars on each row.
    for j in range(rows - i):  # Calculate and print leading spaces to center the current row.
        print(" ", end=" ")  # Print a space without moving to the next line.
    for k in range(1, 2 * i):  # Print an odd number of stars: 1, 3, 5, and so on.
        print("*", end=" ")  # Print a star and stay on the same line.
    print()  # Finish the current row and move to the next line.

for i in range(rows - 1, 0, -1):  # Build the lower half, decreasing the number of stars; skip repeating the widest row.
    for j in range(rows - i):  # Calculate and print leading spaces to center the current row.
        print(" ", end=" ")  # Print a space without moving to the next line.
    for k in range(1, 2 * i):  # Print an odd number of stars, decreasing for each lower row.
        print("*", end=" ")  # Print a star and stay on the same line.
    print()  # Finish the current row and move to the next line.

# Example output when the user enters 4:
#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *