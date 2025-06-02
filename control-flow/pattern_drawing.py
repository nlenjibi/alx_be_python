# pattern_drawing.py

# Prompt user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print stars in a row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
