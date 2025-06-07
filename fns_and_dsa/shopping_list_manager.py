# shopping_list_manager.py

# Array to hold shopping list items
shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. View list")
    print("3. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                item = input("Enter an item to add: ")
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
            elif choice == 2:
                print("Your Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            elif choice == 3:
                print("Exiting Shopping List Manager.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
