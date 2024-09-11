# Function to print a heart shape
def print_heart():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or \
               (row == 1 and col % 3 == 0) or \
               (row == 2) or \
               (row - col == 2) or \
               (row + col == 8):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Call the function
print_heart()
