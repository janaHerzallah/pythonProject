class User:

    def __init__(self, user_id, user_name, date_of_birth, role, active):
        self.user_id = user_id
        self.user_name = user_name
        self.date_of_birth = date_of_birth
        self.role = role
        self.active = active
        self.basket = {}  # Initialize an empty basket as a dictionary
        self.order = 0

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def set_role(self, role):
        self.role = role

    def set_active(self, active):
        self.active = active

    def set_basket(self, basket):
        self.basket = basket

    def set_order(self, order):
        self.order = order

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_role(self):
        return self.role

    def get_active(self):
        return self.active

    def get_basket(self):
        return self.basket

    def get_order(self):
        return self.order

    def add_product_to_basket(self, product_id, quantity):
        if product_id not in self.basket:
            self.basket[product_id] = quantity
        else:
            self.basket[product_id] += quantity


    def to_dict(self):
        # Convert user attributes to a dictionary
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'date_of_birth': self.date_of_birth,
            'role': self.role,
            'active': self.active,
            'basket': self.basket,
            'order': self.order
        }

    def clear_basket(self):
        self.basket.clear()

    def remove_product_from_basket(self, product_id):
        # Check if the product_id is in the basket
        if product_id in self.basket:
            del self.basket[product_id]
            return True
        else:
            return False

    def update_product_quantity_in_basket(self, product_id, new_quantity):
        # Check if the product_id is in the basket
        if product_id in self.basket:
            # Ensure that the new quantity is non-negative
            if new_quantity >= 0:
                self.basket[product_id] = new_quantity
                return True
        return False
