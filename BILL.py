# Grocery Shop Billing System with Categories and Menu

cart = []

# Predefined Categories and Items
categories = {
    "Fruits": ["Apple", "Banana", "Mango", "Orange", "Pineapple"],
    "Dairy": ["Milk", "Cheese", "Butter", "Yogurt"],
    "Vegetables": ["Carrot", "Potato", "Tomato", "Onion", "Spinach"]
}

def show_categories():
    print("\n--- Categories ---")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    print("----------------------")

def show_items(category):
    print(f"\n--- {category} Items ---")
    for idx, item in enumerate(categories[category], 1):
        print(f"{idx}. {item}")
    print("----------------------")

def add_item():
    show_categories()
    category_choice = int(input("Choose a category to view items (1-3): "))
    
    if category_choice not in range(1, 4):
        print("Invalid category choice!")
        return
    
    category_name = list(categories.keys())[category_choice - 1]
    show_items(category_name)
    
    item_choice = int(input(f"Choose an item to add from {category_name} (1-{len(categories[category_name])}): "))
    
    if item_choice not in range(1, len(categories[category_name]) + 1):
        print("Invalid item choice!")
        return
    
    item_name = categories[category_name][item_choice - 1]
    quantity = int(input(f"Enter quantity of {item_name}: "))
    price = float(input(f"Enter price of one {item_name}: "))
    total_price = quantity * price
    cart.append({"name": item_name, "category": category_name, "quantity": quantity, "price": price, "total": total_price})
    print(f"{item_name} added to the cart under category {category_name}!")

def view_cart():
    if not cart:
        print("Your cart is empty!")
        return
    print("\n--- Your Cart ---")
    print(f"{'Item':<10}{'Category':<12}{'Qty':<10}{'Price':<10}{'Total':<10}")
    for item in cart:
        print(f"{item['name']:<10}{item['category']:<12}{item['quantity']:<10}{item['price']:<10.2f}{item['total']:<10.2f}")
    print("----------------------")

def generate_bill():
    if not cart:
        print("Your cart is empty! No bill to generate.")
        return
    view_cart()
    total_bill = sum(item['total'] for item in cart)
    print(f"\nTotal Bill: Rs. {total_bill:.2f}")
    print("Thank you for shopping with us!")

    # Save the bill to a file
    save_bill_to_file(total_bill)

def save_bill_to_file(total_bill):
    with open("bill.txt", "w") as file:
        file.write("--- Grocery Shop Bill ---\n")
        file.write(f"{'Item':<10}{'Category':<12}{'Qty':<10}{'Price':<10}{'Total':<10}\n")
        for item in cart:
            file.write(f"{item['name']:<10}{item['category']:<12}{item['quantity']:<10}{item['price']:<10.2f}{item['total']:<10.2f}\n")
        file.write("----------------------\n")
        file.write(f"Total Bill: Rs. {total_bill:.2f}\n")
        file.write("Thank you for shopping with us!\n")
    print("Bill saved to 'bill.txt' successfully!")

while True:
    print("\nOptions: 1. Add Item  2. View Cart  3. Generate Bill  4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_item()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        generate_bill()
    elif choice == '4':
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.")
