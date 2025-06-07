# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"Added '{item}'.")
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}'.")
            else:
                print(f"Item '{item}' not found in list.")
        elif choice == '3':
            print("\nCurrent Shopping List:")
            if shopping_list:
                for idx, it in enumerate(shopping_list, 1):
                    print(f"{idx}. {it}")
            else:
                print("  [empty]")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
