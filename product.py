# product.py
class Product:
    def __init__(self, product_id, product_name, product_category, price, inventory, supplier, has_on_offer=0, offer_price=0, valid_until=None):
        self.product_id = product_id
        self.product_name = product_name
        self.product_category = product_category
        self.price = price
        self.inventory = inventory
        self.supplier = supplier
        self.has_on_offer = has_on_offer
        self.offer_price = offer_price
        self.valid_until = valid_until

    # Getter methods
    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_product_category(self):
        return self.product_category

    def get_price(self):
        return self.price

    def get_inventory(self):
        return self.inventory

    def get_supplier(self):
        return self.supplier

    def get_has_on_offer(self):
        return self.has_on_offer

    def get_offer_price(self):
        return self.offer_price

    def get_valid_until(self):
        return self.valid_until

    # Setter methods
    # Setter method with validation for product_id
    def set_product_id(self, product_id):
        while True:
            if isinstance(product_id, int) and 100000 <= product_id <= 999999:
                self.product_id = str(product_id).zfill(6)
                break
            else:
                print("Invalid product ID. Product ID must be a 6-digit integer.")
                try:
                    product_id = int(input("Enter a valid 6-digit product ID: "))
                except ValueError:
                    print("Invalid input. Please enter a valid 6-digit integer for product ID.")

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_product_category(self, product_category):
        self.product_category = product_category

    # Setter method with validation for price

    def set_price(self, price):
            while True:
                if price >= 0:
                    self.price = price
                    break
                else:
                    print("Invalid price. Price must be a positive number.")
                    price = float(input("Enter a valid price: "))

        # Setter method with validation for inventory
    def set_inventory(self, inventory):
            while True:
                if inventory >= 0:
                    self.inventory = inventory
                    break
                else:
                    print("Invalid inventory. Inventory must be a non-negative integer.")
                    inventory = int(input("Enter a valid inventory: "))

    def set_supplier(self, supplier):
        self.supplier = supplier

    def set_has_on_offer(self, has_on_offer):
        self.has_on_offer = has_on_offer

    def set_offer_price(self, offer_price):
        self.offer_price = offer_price

    def set_valid_until(self, valid_until):
        self.valid_until = valid_until

    # Implement methods to set and get product attributes

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_category': self.product_category,
            'price': self.price,
            'inventory': self.inventory,
            'supplier': self.supplier,
            'has_on_offer': self.has_on_offer,
            'offer_price': self.offer_price,
            'valid_until': self.valid_until,
        }
