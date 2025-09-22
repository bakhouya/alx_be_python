# ========================================================================
# imports datetime  and timedelta from the datetime model
from datetime import datetime, timedelta
# ========================================================================

# ========================================================================
# her we define a function to display the current date and time 
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date
# ========================================================================

# ========================================================================
# here we difine a function to calculate future date by adding a specific number of days to the current date 
def calculate_future_date(days: int):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date
# ========================================================================

# ========================================================================
def main():
    # dislay the current date and time , i mean we call the function display_current_datetime
    display_current_datetime()
    # here we ask the user to enter the number of day they want to add to the current date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    # if the user enter a value that is not an integer, we catch the ValueError
    except ValueError:
        print(" Please enter a valid integer for days.")
# ========================================================================

if __name__ == "__main__":
    main()