

# ===============================================================================================
# Here we ask the user to enter a number, which will be the number of rows and columns.
size = int(input("Enter the size of the pattern: "))
# ===============================================================================================

# ===============================================================================================
# We set the row counter to 0 so that we can use it in the while loop to count the number of rows
row = 0

# Here we run our while loop as long as the row counter is less than the number entered by the user
while row < size:
    
    #Here we use a for loop to print the '*' character the number of times entered by the user
    for _ in range(size):
        print("*", end="")
    print()
    # Here we control the row and increment it by 1 in each cycle to keep track of the number of iterations
    row += 1
# ===============================================================================================
