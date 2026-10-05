rows = int(input("Enter the row size for the pattern: "))  # Ask the user for the butterfly's size and convert the input to an integer.

for i in range(1, rows + 1):  # Build the upper half, increasing the number of stars on each row.
    for j in range(1, i + 1):  # Print the left wing's stars for this row.
        print("*", end=" ")  # Print a star and stay on the same line.
    for j in range(2 * (rows - i)):  # Calculate how many spaces are needed between the wings.
        print(" ", end=" ")  # Print a space without moving to the next line.
    for j in range(1, i + 1):  # Print the right wing's stars for this row.
        print("*", end=" ")  # Print a star and stay on the same line.
    print()  # Finish this row and move to the next line.

for i in range(rows, 0, -1):  # Build the lower half, decreasing the number of stars on each row; this repeats the widest row.
    for j in range(1, i + 1):  # Print the left wing's stars for this row.
        print("*", end=" ")  # Print a star and stay on the same line.
    for j in range(2 * (rows - i)):  # Calculate how many spaces are needed between the wings.
        print(" ", end=" ")  # Print a space without moving to the next line.
    for j in range(1, i + 1):  # Print the right wing's stars for this row.
        print("*", end=" ")  # Print a star and stay on the same line.
    print()  # Finish this row and move to the next line.

# Example output when the user enters 4:
# *             *
# * *         * *
# * * *     * * *
# * * * * * * * *
# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *