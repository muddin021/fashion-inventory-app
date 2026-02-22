import json
import os

DATA_FILE = "inventory.json"

def load_inventory():
    """Load inventory from a JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_inventory(inventory):
    """Save inventory to a JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(inventory, f, indent=2)

def add_item(inventory):
    print("\n--- Add Item ---")
    name = input("Item name: ").strip()
    category = input("Category (e.g., Tops, Shoes): ").strip()

    while True:
        try:
            price = float(input("Price: $").strip())
            if price < 0:
                print("Price can't be negative.")
                continue
            break
        except ValueError:
            print("Enter a valid number for price.")

    while True:
        try:
            qty = int(input("Quantity: ").strip())
            if qty < 0:
                print("Quantity can't be negative.")
                continue
            break
        except ValueError:
            print("Enter a valid whole number for quantity.")

    for item in inventory:
        if item["name"].lower() == name.lower() and item["category"].lower() == category.lower():
            item["quantity"] += qty
            print(f"Updated quantity for {item['name']} ({item['category']}).")
            save_inventory(inventory)
            return

    inventory.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": qty
    })

    save_inventory(inventory)
    print("Item added!")

def view_inventory(inventory):
    print("\n--- Inventory ---")
    if not inventory:
        print("No items yet.")
        return

    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} | {item['category']} | ${item['price']:.2f} | Qty: {item['quantity']}")

def update_quantity(inventory):
    print("\n--- Update Quantity ---")
    if not inventory:
        print("No items to update.")
        return

    view_inventory(inventory)

    while True:
        try:
            idx = int(input("Enter item number to update: ").strip())
            if idx < 1 or idx > len(inventory):
                print("Invalid item number.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            new_qty = int(input("Enter new quantity: ").strip())
            if new_qty < 0:
                print("Quantity can't be negative.")
                continue
            break
        except ValueError:
            print("Enter a valid whole number.")

    inventory[idx - 1]["quantity"] = new_qty
    save_inventory(inventory)
    print("Quantity updated!")

def remove_item(inventory):
    print("\n--- Remove Item ---")
    if not inventory:
        print("No items to remove.")
        return

    view_inventory(inventory)

    while True:
        try:
            idx = int(input("Enter item number to remove: ").strip())
            if idx < 1 or idx > len(inventory):
                print("Invalid item number.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    removed = inventory.pop(idx - 1)
    save_inventory(inventory)
    print(f"Removed: {removed['name']} ({removed['category']})")

def total_value(inventory):
    total = sum(item["price"] * item["quantity"] for item in inventory)
    print(f"\nTotal inventory value: ${total:.2f}")

def menu():
    inventory = load_inventory()

    while True:
        print("\n==============================")
        print("   MINI FASHION INVENTORY APP  ")
        print("==============================")
        print("1) Add item")
        print("2) View inventory")
        print("3) Update quantity")
        print("4) Remove item")
        print("5) Total inventory value")
        print("6) Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            total_value(inventory)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Pick 1-6.")

if __name__ == "__main__":
    menu()
