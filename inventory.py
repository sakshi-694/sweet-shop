# inventory.py

class SweetItem:
    def _init_(self, sid, name, category, price, stock):
        self.id = sid
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

class InventoryManager:
    def _init_(self):
        self.products = []
        self.next_id = 1
        self.seed_items()

    def seed_items(self):
        self.add_new("Kaju Katli", "Mithai", 18, 20)
        self.add_new("Black Forest", "Pastry", 35, 10)
        self.add_new("5 Star", "Chocolate", 25, 15)

    def add_new(self, name, category, price, quantity):
        item = SweetItem(self.next_id, name, category, price, quantity)
        self.products.append(item)
        self.next_id += 1

    def remove_by_id(self, item_id):
        self.products = [p for p in self.products if p.id != item_id]

    def list_all(self):
        return self.products

    def search_items(self, name=None, category=None, min_price=None, max_price=None):
        result = self.products
        if name:
            result = [p for p in result if name.lower() in p.name.lower()]
        if category:
            result = [p for p in result if category.lower() == p.category.lower()]
        if min_price is not None and max_price is not None:
            result = [p for p in result if min_price <= p.price <= max_price]
        return result

    def purchase(self, item_id, quantity):
        for item in self.products:
            if item.id == item_id:
                if item.stock >= quantity:
                    item.stock -= quantity
                    total = item.price * quantity
                    return item.name, quantity, total, item.stock
                else:
                    raise ValueError(f"Only {item.stock} available in stock.")
        raise ValueError("Item not found.")

    def restock(self, item_id, quantity):
        for item in self.products:
            if item.id == item_id:
                item.stock += quantity
                return item.stock
        raise ValueError("Item not found.")