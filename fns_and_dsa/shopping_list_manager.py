# ========================================================================
# Here, we create a function that displays the program name 
# and the instructions to the user, which they can follow in the program
def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
# ========================================================================

# ========================================================================
# Here, we wrote a main function that runs the code as long as the user hasn’t stopped the execution
def main():
    # initialize an empty shopping list
    shopping_list = []  
    while True:
        # Here, we call the function we created above to display the menu
        display_menu()  
        # Here, we ask the user to enter their choice or the operation they want to perform
        choice = input("Enter your choice: ") 

        # ========================================================================
        # if the user enters '1' that mean user want to add new items to the shopping list
        if choice == '1':
            # Her we ask user to enter the item they want to add
            item = input("Enter the item to add: ").strip()
            # If user add new item, we append it to the shopping list and print a cenfirmation message
            if item:
                shopping_list.append(item)
                print("Added new item successfully")
            else:
                print("error: Item name must not be empty")
        # ========================================================================
        
        # ========================================================================
        # If the user enters '2' that mean user want to remove an item from the shopping list
        elif choice == '2':
            # Here we ask user to enter the item they want to remove
            item = input("Enter the item to remove: ").strip()
            # If this item is in the shopping list, we remove it and print a confirmation message
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        # ========================================================================

        # ========================================================================
        elif choice == '3':
            # If the user enters '3' that mean user want to display the shopping list 
            if shopping_list:
                print("\n Your Shopping List:")
                # her we loop through the shopping list and print each item with its index
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            # If the shopping list is empty, we print a message indicating that 
            else:
                print("Your shopping list is empty.")
        # ========================================================================

        # ========================================================================
        # If the user enters '4' that mean user want to exit the program 
        elif choice == '4':
            print("Goodbye!")
            break
        # ========================================================================

        # ========================================================================
        # If the user enters anythinsg , we print an error message indicating that
        else:
            print("Invalid choice. Please try again.")
        # ========================================================================


# ========================================================================

if __name__ == "__main__":
    main()
