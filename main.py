# main.py

from inventory import InventoryManager

def show_items(items):
    if not items:
        print("No items found.")
        return
    for item in items:
        print(f"ID: {item.id} | Name: {item.name} | Category: {item.category} | Price: ₹{item.price} | Stock: {item.stock}")

def main():
    inv = InventoryManager()

    while True:
        print("\n=== Sweet Shop Console ===")
        print("1. View All Items")
        print("2. Add New Sweet")
        print("3. Delete Sweet by ID")
        print("4. Search Sweets")
        print("5. Buy Sweet")
        print("6. Restock Sweet")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            all_items = inv.list_all()
            show_items(all_items)

        elif choice == '2':
            name = input("Enter sweet name: ")
            cat = input("Enter category: ")
            try:
                price = int(input("Enter price: "))
                qty = int(input("Enter quantity: "))
                inv.add_new(name, cat, price, qty)
                print("Sweet added successfully.")
            except:
                print("Invalid input for price or quantity.")

        elif choice == '3':
            try:
                id_to_remove = int(input("Enter sweet ID to remove: "))
                inv.remove_by_id(id_to_remove)
                print("Sweet removed.")
            except:
                print("Invalid ID.")

        elif choice == '4':
            name = input("Search by name (leave blank to skip): ")
            cat = input("Search by category (leave blank to skip): ")
            try:
                min_price = int(input("Minimum price (or 0): ") or 0)
                max_price = int(input("Maximum price (or 0): ") or 0)
            except:
                min_price = max_price = None

            results = inv.search_items(
                name=name or None,
                category=cat or None,
                min_price=min_price if max_price > 0 else None,
                max_price=max_price if max_price > 0 else None
            )
            show_items(results)

        elif choice == '5':
            try:
                item_id = int(input("Enter sweet ID to buy: "))
                qty = int(input("Enter quantity: "))
                name, bought, total, left = inv.purchase(item_id, qty)
                print(f"Purchased {bought} x {name} for ₹{total}. Remaining stock: {left}")
            except Exception as e:
                print("Error:", e)

        elif choice == '6':
            try:
                restock_id = int(input("Enter ID to restock: "))
                add_qty = int(input("Enter quantity to add: "))
                new_stock = inv.restock(restock_id, add_qty)
                print(f"Updated stock: {new_stock}")
            except Exception as e:
                print("Error:", e)

        elif choice == '7':
            print("Exiting Sweet Shop. Goodbye!")
            break

        else:
            print("Invalid choice.")

if _name_ == "_main_":
    main()