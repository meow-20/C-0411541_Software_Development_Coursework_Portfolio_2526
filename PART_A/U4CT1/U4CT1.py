import csv

FILENAME = "inventory.csv"

# Load inventory from file
def load_inventory():
    inventory = []
    try:
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                name, quantity, price = row
                inventory.append({
                    "name": name,
                    "quantity": int(quantity),
                    "price": float(price)
                })
    except FileNotFoundError:
        pass
    return inventory


# Save inventory to file
def save_inventory(inventory):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        for item in inventory:
            writer.writerow([item["name"], item["quantity"], item["price"]])


# Display inventory
def display_inventory(inventory):
    print("\n--- Inventory ---")
    if not inventory:
        print("Inventory is empty.")
    for item in inventory:
        print(f"{item['name']} | Quantity: {item['quantity']} | Price: £{item['price']}")


# Main program
inventory = load_inventory()

while True:
    print("\nInventory Menu:")
    print("1. Add product")
    print("2. Update quantity")
    print("3. Display inventory")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        inventory.append({
            "name": name,
            "quantity": quantity,
            "price": price
        })
        save_inventory(inventory)
        print("Product added successfully!")

    elif choice == "2":
        name = input("Enter product name to update: ")
        for item in inventory:
            if item["name"].lower() == name.lower():
                item["quantity"] = int(input("Enter new quantity: "))
                save_inventory(inventory)
                print("Quantity updated!")
                break
        else:
            print("Product not found.")

    elif choice == "3":
        display_inventory(inventory)

    elif choice == "4":
        print("Exiting inventory system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
