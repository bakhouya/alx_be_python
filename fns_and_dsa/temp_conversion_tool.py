# ========================================================================
# Here we define constants for the conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
# ========================================================================

# ========================================================================
# here we define a function to convert fahrenheit to celsius
def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
# ========================================================================

# ========================================================================
# here we define a function to convert celsius to fahrenheit
def convert_to_fahrenheit(celsius: float) -> float:
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
# ========================================================================


# ========================================================================
def main():
    try:
        # here we ask the user to enter the temperature the want to convert
        temp_input = input("Enter the temperature to convert: ").strip()
        # here we try to convert the input to a float
        temperature = float(temp_input)  

        # here we ask the user to specify the unit of the temperature they entred 
        # C for celsius  | F for fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # if unit or if user enter C that mean user want to convert celsius to fahrenheit
        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        # if unit or if user enter F that mean user want to convert fahrenheit to celsius
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        # if user enter anything else we print an error message indicating that
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
# ========================================================================

if __name__ == "__main__":
    main()
