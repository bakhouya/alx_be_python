
# ==============================================================================================
# Here we have a function called perform_operation that takes 3 arguments: number1, number2, 
# and operation. Both number1 and number2 are floats, while operation is a string."
def perform_operation(num1 , num2, operation):
    # If the operation is 'add', meaning addition, we return the sum of number1 and number2
    if operation == "add":
        return num1 + num2 
    # If the operation is 'subtract', meaning subtraction, we return number1 - number2
    elif operation == "subtract":
        return num1 - num2
    # If the operation is 'multiply', meaning multiplication, we return number1 * number2
    elif operation == "multiply":
        return num1 * num2
    # If the operation is 'divide', we check if number2 == 0. If it is, we return an error message. Otherwise, 
    # if number2 != 0, we return number1 / number2.
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    # Finally, if the operation does not match any of the conditions above, we return an error message
    else:
        return "Error: Invalid operation"
# ==============================================================================================