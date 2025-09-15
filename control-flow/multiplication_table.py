
# ===============================================================================================
# Here we ask the user to enter a number in the input field, 
# and we check to make sure they only enter a number
number = int(input("Enter a number to see its multiplication table: "))
# ===============================================================================================

# ===============================================================================================
# Here we use a for loop from 1 to 11 to multiply the number and perform the multiplication operation
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

# ===============================================================================================