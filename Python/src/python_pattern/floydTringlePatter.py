rows = int(input("Enter the row size for the pattern: "))
num = 1
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(num, end=" ")  # Print numbers in sequence
        num += 1
    print()
    
   # /*
    # Output:
    # Enter the row size for the pattern: 4
    # 1 
    # 2 3 
    # 4 5 6 
    # 7 8 9 10 
     # 