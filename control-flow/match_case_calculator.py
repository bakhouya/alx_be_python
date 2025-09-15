


# ===============================================================================================
# Here we are receiving two numbers and the type of operation from the user, 
# then storing them in variables to use later in the calculation
number1 = float(input("Enter the first number : "))
number2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
# ===============================================================================================

# ===============================================================================================
# Here we will apply the chosen operation to the numbers based on the type of operation selected by the user
match operation:
    case "+":
        result = number1 + number2
        print(f"The result is {result}")
    case "-":
        result = number1 - number2
        print(f"The result is {result}")
    case "*":
        result = number1 * number2
        print(f"The result is {result}")
    case "/":
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            result = number1 / number2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose one of (+, -, *, /).")
# ===============================================================================================
