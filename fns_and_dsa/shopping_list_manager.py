def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            if item:
                shopping_list.append(item)
                print("Added!")
            else:
                print("Invalid item name")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            try:
                item_index = shopping_list.index(item)
                del shopping_list[item_index]
                print("Removed!")
            except ValueError as e:
                print("Item not found")
        elif choice == '3':
            # Display the shopping list
            print("------------")
            for item in shopping_list:
                print(item)
            print("------------")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()