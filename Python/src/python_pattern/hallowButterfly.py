rows = int(input("Enter the row size for the pattern: "))  # Ask the user for the pattern size and convert the input to an integer.

for i in range(1, rows + 1):  # Build the upper half, increasing the wing width from 1 star to rows stars.
    for j in range(1, i + 1):  # Visit each position in the left wing of the current row.
        if j == 1 or j == i:  # Check whether this position is the first or last in the wing.
            print("*", end=" ")  # Print a star at the wing's edge without moving to a new line.
        else:  # Run when this position is inside the wing, not at an edge.
            print(" ", end=" ")  # Print a blank position to make the wing hollow.
    for j in range(2 * (rows - i)):  # Calculate the number of spaces between the left and right wings.
        print(" ", end=" ")  # Print a space between the wings without moving to a new line.
    for j in range(1, i + 1):  # Visit each position in the right wing of the current row.
        if j == 1 or j == i:  # Check whether this position is the first or last in the wing.
            print("*", end=" ")  # Print a star at the wing's edge without moving to a new line.
        else:  # Run when this position is inside the wing, not at an edge.
            print(" ", end=" ")  # Print a blank position to make the wing hollow.
    print()  # Finish the current row and move to the next line.

for i in range(rows, 0, -1):  # Build the lower half, decreasing the wing width from rows stars to 1.
    for j in range(1, i + 1):  # Visit each position in the left wing of the current row.
        if j == 1 or j == i:  # Check whether this position is the first or last in the wing.
            print("*", end=" ")  # Print a star at the wing's edge without moving to a new line.
        else:  # Run when this position is inside the wing, not at an edge.
            print(" ", end=" ")  # Print a blank position to make the wing hollow.
    for j in range(2 * (rows - i)):  # Calculate the number of spaces between the left and right wings.
        print(" ", end=" ")  # Print a space between the wings without moving to a new line.
    for j in range(1, i + 1):  # Visit each position in the right wing of the current row.
        if j == 1 or j == i:  # Check whether this position is the first or last in the wing.
            print("*", end=" ")  # Print a star at the wing's edge without moving to a new line.
        else:  # Run when this position is inside the wing, not at an edge.
            print(" ", end=" ")  # Print a blank position to make the wing hollow.
    print()  # Finish the current row and move to the next line.

# Example output when the user enters 4:
# *             *
# * *         * *
# *   *     *   *
# *     * *     *
# *     * *     *
# *   *     *   *
# * *         * *
# *             *