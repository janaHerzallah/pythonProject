# Import necessary classes and modules
import EcommerceModule
from User import User
from product import Product


class ECommerceSystem:

    def __init__(self):

        # Initialize the E-commerce system, load data from files, create objects, etc.

        self.products = []  # This list will hold Product objects

        self.users = []  # This list will hold User objects

    def run(self):

        file2_path = "products.txt"
        self.products = self.read_products_file(file2_path)

        file_path = "users.txt"
        # save users.txt users to users list
        self.users = self.read_users_file(file_path)


        self.display_users()
        self.display_products()

        print("******************************************")
        print("*    Welcome to the E-Commerce System    *")
        print("******************************************")
        print()
        # Ask for the user ID
        user_id = input("Enter your user ID: ")
        print()
        # print welcome statement includes the user's name
        user = self.find_user_by_id(user_id)
        if user is not None:
            self.current_user_role = user.get_role()
            user_name = user.get_user_name()


            if user.get_role() == 1:
                print(f"Welcome, {user_name}")
                print("Enjoy your shopping ..")  # This is "Enjoy your shopping!" in Arabic
                print()
                self.check_notifications(user_id)
            else:
                print(f"Welcome, E-commerce Administrator {user_name}.")

        self.current_user_role = self.get_user_role(user_id)


        while True:
            # Display the menu and get the selected option
            selected_option = self.display_menu()  # Use 'self' to call the instance method

            if self.current_user_role == 1:
                # Shopper can only access options 7-12
                if selected_option not in (7, 9, 10, 11, 12, 16):
                    # Print an access denied message for unauthorized shoppers
                    print()
                    print("You are not authorized to perform this action!")
                    continue  # Continue the loop to prompt for another option

            elif self.current_user_role == 0:
                # Admin can only access options 1-6, 13-16
                if selected_option not in (1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 16):
                    # Print an access denied message for unauthorized administrators
                    print()
                    print("You are not authorized to perform this action!")
                    continue  # Continue the loop to prompt for another option



            if selected_option == 1:
                # Add product logic
                self.add_product()
                # Ask if the user wants to continue using the menu
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass
            elif selected_option == 2:
                # Place an item on sale logic
                self.place_item_on_sale()
                # Ask if the user wants to continue using the menu
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass

            elif selected_option == 3:
                # Update product logic
                self.update_product()
                # Ask if the user wants to continue using the menu
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass

            elif selected_option == 4:
                # Add new user (admin-only) logic
                self.add_new_user()
                # Ask if the user wants to continue using the menu
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass

            elif selected_option == 5:
                # Update user (admin-only) logic
                self.update_user()
                # Ask if the user wants to continue using the menu
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass

            elif selected_option == 6:
                # Display all users (admin-only) logic
                self.display_users()
                # Ask if the user wants to continue using the menu
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass

            elif selected_option == 7:
                # List products (admin and shopper) logic
                self.list_products()
                # Ask if the user wants to continue using the menu
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass

            elif selected_option == 8:
                # List shoppers (admin) logic
                self.list_all_shoppers()
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass


            elif selected_option == 9:

                self.add_product_to_basket(user_id)

                if not self.ask_to_continue():
                    print("Exiting the system.")

                    break

                pass

            elif selected_option == 10:
                # Display basket (shopper-only) logic
                self.display_basket(user_id)
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass
            elif selected_option == 11:
                # Update basket (shopper-only) logic
                self.update_basket(user_id)
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass
            elif selected_option == 12:
                # Place order (shopper-only) logic
                self.place_order(user_id)
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass
            elif selected_option == 13:
                # Execute order (admin-only) logic
                self.execute_order(user_id)
                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass
            elif selected_option == 14:
                # Save products to a file (admin-only) logic
                file_name = input("Enter the name of the text file (e.g., myOUTPUTS.txt): ")
                EcommerceModule.save_products_to_file(self.products,file_name)

                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass
            elif selected_option == 15:
                # Save users to a text file (admin-only) logic
                file_name = input("Enter the name of the text file (e.g., myOUTPUTS.txt): ")
                EcommerceModule.save_users_to_file(self.users, file_name)

                if not self.ask_to_continue():
                    print("Exiting the system.")
                    break
                pass

            elif selected_option == 16:
                print("Exiting the system.")
                break

    def read_users_file(self, file_path):
        users = []

        try:
            with open(file_path, "r") as file:
                for line in file:
                    user_data = line.strip().split(";")
                    if len(user_data) == 7:  # Ensure there are 7 fields in each line
                        # Extract user data fields
                        user_id, user_name, dob, role, active, basket_data, order = user_data

                        # Convert role to 0 for "admin" and 1 for "shopper"
                        role = 0 if role.lower() == "admin" else 1

                        # Parse basket data into a dictionary
                        basket = self.parse_basket_data(basket_data)

                        # Create a User object
                        user = User(user_id, user_name, dob, role, active)
                        user.set_basket(basket)
                        user.set_order(int(order))

                        # Append the User object to the list of users
                        users.append(user)
                    else:
                        # Handle data format errors
                        print(f"Invalid user data format in line: {line.strip()}")
        except FileNotFoundError:
            # Handle the case where the specified file is not found
            print(f"File '{file_path}' not found.")

        return users

    def parse_basket_data(self, basket_data):
        # Initialize an empty basket as a dictionary
        basket = {}

        # Check if basket data is not empty and properly formatted
        if basket_data and basket_data.startswith('{') and basket_data.endswith('}'):
            # Remove the curly braces and split by ',' to get key-value pairs
            basket_items = basket_data[1:-1].split(',')

            for item in basket_items:
                # Check if there is a ':' in the item
                if ':' in item:
                    # Split each key-value pair by ':' to separate the product_id and quantity
                    product_id, quantity = item.split(':')
                    # Assign the quantity (converted to int) to the product_id as the key
                    basket[product_id.strip()] = int(quantity.strip())
                else:

                    pass

        return basket



    def read_products_file(self, file_path):
        # Create an empty list to store product objects
        products = []

        try:
            # Open the file for reading
            with open(file_path, "r") as file:
                # Read each line in the file
                for line in file:
                    # Split the line into a list using semicolons as separators
                    product_data = line.strip().split(";")

                    # Check if there are at least 7 fields in each line
                    if len(product_data) >= 7:
                        # Parse the product data from the list
                        product_id = product_data[0]
                        product_name = product_data[1]
                        product_category = product_data[2]
                        price = float(product_data[3])
                        inventory = int(product_data[4])
                        supplier = product_data[5]
                        has_on_offer = int(product_data[6])

                        # Check if the product has an offer
                        if has_on_offer == 1:
                            offer_price = float(product_data[7])
                            valid_until = product_data[8]
                        else:
                            offer_price = 0  # No offer price for products without an offer
                            valid_until = None  # No validity date for products without an offer

                        # Create a Product object using the parsed data
                        product = Product(
                            product_id, product_name, product_category, price,
                            inventory, supplier, has_on_offer, offer_price, valid_until
                        )

                        # Append the product to the list
                        products.append(product)
                    else:
                        # Display an error message for lines with invalid data format
                        print(f"Invalid product data format in line: {line.strip()}")
        except FileNotFoundError:
            # Handle the case where the file is not found
            print(f"File '{file_path}' not found.")

        # Return the list of product objects
        return products

    #function to find the user according to  passing id
    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.get_user_id() == user_id:
                return user
        return None


    def get_user_role(self, user_id):
        while True:
            if len(user_id) != 6 or not user_id.isdigit():
                print("Invalid user ID format. Please enter a 6-digit integer.")
            else:
                user_ids = [user.get_user_id() for user in self.users]
                if user_id in user_ids:
                    for user in self.users:
                        if user.get_user_id() == user_id:
                            return user.get_role()
                else:
                    print("User ID does not exist. Please enter a valid user ID.")

            user_id = input("Enter your user ID: ")



    # Function to display the menu and get user's choice
    def display_menu(self):
        print("\nMenu Options:")
        print("1. Add product (admin-only)")
        print("2. Place an item on sale (admin-only)")
        print("3. Update product (admin-only)")
        print("4. Add a new user (admin-only)")
        print("5. Update user (admin-only)")
        print("6. Display all users (admin-only)")
        print("7. List products (admin and shopper)")
        print("8. List shoppers (admin)")
        print("9. Add product to the basket (shopper-only)")
        print("10. Display basket (shopper-only)")
        print("11. Update basket (shopper-only)")
        print("12. Place order (shopper-only)")
        print("13. Execute order (admin-only)")
        print("14. Save products to a file (admin-only)")
        print("15. Save users to a text file (admin-only)")
        print("16. Exit")
        print()

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 16:
                    return choice
                else:
                    print("Invalid choice. Please enter a valid option (1-16).")
            except ValueError:
                print("Invalid input. Please enter a valid option (1-16).")





    def display_users(self):
        print("\nList of Users:")
        for user in self.users:
            print(f"User ID: {user.get_user_id()}")
            print(f"User Name: {user.get_user_name()}")
            print(f"Date of Birth: {user.get_date_of_birth()}")
            print(f"Role: {user.get_role()}")
            print(f"Active: {user.active}")
            print(f"Basket: {user.get_basket()}")
            print(f"Order: {user.get_order()}")
            print("=" * 40)

    def display_products(self):
        if not self.products:
            print("No products to display.")
        else:
            for product in self.products:
                print("Product ID:", product.get_product_id())
                print("Product Name:", product.get_product_name())
                print("Product Category:", product.get_product_category())
                print("Price:", f"${product.get_price():.2f}")
                print("Inventory:", product.get_inventory())
                print("Supplier:", product.get_supplier())
                print("Has on Offer:", "Yes" if product.get_has_on_offer() == 1 else "No")

                if product.get_has_on_offer() == 1:
                    print("Offer Price:", f"${product.get_offer_price():.2f}")
                    print("Valid Until:", product.get_valid_until())

                print("=" * 40)


    def get_user_id(self):
        while True:
            try:
                user_id = input("Enter your user ID: ")
                if len(user_id) == 6 and user_id.isdigit():
                    self.current_user_id = user_id
                    return
                else:
                    print("Invalid user ID format. Please enter a 6-digit integer.")
            except ValueError:
                print("Invalid input. Please enter a valid user ID.")

        # Define a function to ask the user if they want to continue using the menu


    def ask_to_continue(self):
        while True:
            exit_choice = input("Do you want to do anything else? (yes/no): ").strip().lower()
            if exit_choice == "yes":
                return True
            elif exit_choice == "no":
                return False
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")


    def add_new_user(self):
        user_id = input("Enter user ID (6-digit integer): ")

        # Validate user ID
        while not self.validate_user_id(user_id):
            user_id = input("Enter user ID (6-digit integer): ")

        user_name = input("Enter user name: ")
        dob = input("Enter date of birth (dd/mm/yyyy): ")

        role_input = None
        while role_input is None:
            try:
                role_input = int(input("Enter role (0 for admin, 1 for shopper): "))
                role = self.validate_role(role_input)
            except ValueError:
                print("Invalid input. Please enter 0 for admin or 1 for shopper.")

        active_input = None
        while active_input is None:
            active_input = input("Enter active status (0 for inactive, 1 for active): ")
            active = self.validate_active(active_input)

        if role and active:
            # Create a new User object
            user = User(user_id, user_name, dob, role, active)

            # Append the user to the list of users
            self.users.append(user)

            # Write the user to the 'users.txt' file
            with open("users.txt", "a") as file:
                user_data = f"{user.get_user_id()};{user.get_user_name()};{user.get_date_of_birth()};" \
                            f"{user.get_role()};{user.get_active()};{user.get_basket()};{user.get_order()}\n"
                file.write(user_data)

    def validate_user_id(self, user_id):
        if not (user_id.isdigit() and len(user_id) == 6):
            print("Invalid user ID format. User ID must be a 6-digit integer.")
            return False

        # Check if the user ID is unique
        for user in self.users:
            if user.get_user_id() == user_id:
                print("User ID is not unique. Please enter a unique 6-digit integer.")
                return False

        return True

    def validate_role(self, role_input):
        while True:
            if role_input == 0:
                return "admin"
            elif role_input == 1:
                return "shopper"
            else:
                print("Invalid role input. Please enter 0 for admin or 1 for shopper.")
                role_input = int(input("Enter role (0 for admin, 1 for shopper): "))

    def validate_active(self, active_input):
        while True:
            if active_input in ("0", "1"):
                return active_input
            else:
                print("Invalid active status input. Please enter 0 for inactive or 1 for active.")
                active_input = input("Enter active status (0 for inactive, 1 for active): ")

    def add_product(self):
        print("Add Product:")
        while True:
            product_id = input("Enter product ID (6-digit integer): ")

            # Validate product ID format and uniqueness
            if not (product_id.isdigit() and len(product_id) == 6):
                print("Invalid product ID format. Please enter a 6-digit integer.")
                continue
            if self.find_product_by_id(product_id):
                print("Product ID already exists. Please enter a unique 6-digit integer.")
                continue

            product_name = input("Enter product name: ")
            product_category = input("Enter product category: ")
            price = input("Enter product price (in dollars): ")
            inventory = input("Enter inventory (number of items available): ")
            supplier = input("Enter supplier/company name: ")

            # Validate Has_on_offer flag
            while True:
                has_on_offer = input("Is the product on sale? (0 for no, 1 for yes): ")
                if has_on_offer not in ("0", "1"):
                    print("Invalid input. Please enter '0' for no or '1' for yes.")
                else:
                    break

            if has_on_offer == "1":
                offer_price = input("Enter offer price (in dollars): ")
                valid_until = input("Enter valid until date (yyyy-mm-dd): ")
            else:
                # If the product is not on sale, set offer price to 0 and valid_until to None
                offer_price = "0"
                valid_until = None

            # Create a new Product object
            product = Product(
                product_id, product_name, product_category, float(price),
                int(inventory), supplier, int(has_on_offer), float(offer_price), valid_until
            )

            # Add the product to the list
            self.products.append(product)

            # Write the product data to the 'products.txt' file
            # Write the product data to the 'products.txt' file
            with open("products.txt", "a") as file:
                if has_on_offer == "1":
                    product_data = f"{product_id};{product_name};{product_category};{price};" \
                                   f"{inventory};{supplier};{has_on_offer};{offer_price};{valid_until}\n"
                else:
                    product_data = f"{product_id};{product_name};{product_category};{price};" \
                                   f"{inventory};{supplier};{has_on_offer}\n"
                file.write(product_data)

            print("Product has been added successfully.")
            break  # Exit the loop after adding the product


    def place_item_on_sale(self):
        # Ask the admin to enter the product ID
        product_id = input("Enter the product ID (6-digit integer): ")

        # Validate product ID format
        while not (product_id.isdigit() and len(product_id) == 6):
            print("Invalid product ID format. Please enter a 6-digit integer.")
            product_id = input("Enter the product ID (6-digit integer): ")

        # Check if the product ID exists
        product = self.find_product_by_id(product_id)
        if product is None:
            print("Product with the given ID does not exist.")
            cancel_choice = input("Do you want to cancel this choice? (yes/no): ").strip().lower()
            if cancel_choice == "yes":
                return  # Admin cancels the choice
            elif cancel_choice == "no":
                # Admin can enter a different product ID
                return self.place_item_on_sale()
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                return self.place_item_on_sale()

        # Check if the product already has an offer
        if product.get_has_on_offer() == 1:
            print("This product is already on sale.")
            return

        # Set the Has_on_offer flag of the product to one
        product.set_has_on_offer(1)

        # Ask the admin to enter the offer price
        offer_price = input("Enter the offer price: ")



        while not (offer_price.isdigit() or (offer_price.replace('.', '', 1).isdigit() and float(offer_price) > 0)):
            print("Invalid offer price. Please enter a positive numeric value.")
            offer_price = input("Enter the offer price: ")

        offer_price = float(offer_price)  # Convert the valid input to a float

        # Set the offer price attribute of the product
        product.set_offer_price(float(offer_price))

        # Ask the admin to enter the valid until date
        valid_until = input("Enter the valid until date (yyyy-mm-dd): ")

        # You can add further validation for the date format here

        # Set the valid until date attribute of the product
        product.set_valid_until(valid_until)

        # Update the product data in the products list
        for p in self.products:
            if p.get_product_id() == product_id:
                p.set_has_on_offer(1)
                p.set_offer_price(float(offer_price))
                p.set_valid_until(valid_until)

        # Write the updated product data back to the 'products.txt' file
        with open("products.txt", "w") as file:

                for product in self.products:
                    if product.get_has_on_offer() == 1:
                        product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                       f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()};{product.get_offer_price()};{product.get_valid_until()}\n"
                    else:
                        product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                       f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()}\n"
                    file.write(product_data)
                print("Product has been placed on sale successfully.")





    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_product(self):
        print("Update Product:")
        product_id = input("Enter the product ID to update (6-digit integer): ")

        # Check if the product exists
        product = self.find_product_by_id(product_id)
        if product is None:
            print("Product with the given ID does not exist.")
            return

        while True:
            print("Select the attribute to update:")
            print("1. Product Name")
            print("2. Product Category")
            print("3. Price")
            print("4. Inventory")
            print("5. Supplier")
            print("6. Has on Offer")
            print("7. Offer Price (if on offer)")
            print("8. Valid Until Date (if on offer)")
            print("9. Finish Updating")

            choice = input("Enter your choice: ")

            if choice == "1":
                product_name = input("Enter new product name: ")
                product.set_product_name(product_name)
                self.up(product, product_id)
            elif choice == "2":
                product_category = input("Enter new product category: ")
                product.set_product_category(product_category)
                self.up(product, product_id)
            elif choice == "3":

                while True:
                    price_str = input("Enter new product price (in dollars): ")
                    try:
                        price = float(price_str)
                        if price >= 0:
                            product.set_price(price)
                            self.up(product, product_id)
                            break
                        else:
                            print("Invalid input. Please enter a valid non-negative price.")
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric price.")


            elif choice == "4":
                while True:
                    inventory = input("Enter new inventory (number of items available): ")
                    if inventory.isdigit() and int(inventory) >= 0:
                        product.set_inventory(int(inventory))
                        self.up(product, product_id)
                        break
                    else:
                        print("Invalid input. Please enter a valid non-negative inventory.")
            elif choice == "5":
                supplier = input("Enter new supplier/company name: ")
                product.set_supplier(supplier)
                self.up(product, product_id)


            elif choice == "6":

                while True:

                    has_on_offer_str = input("Is the product on sale? (0 for no, 1 for yes): ")

                    if has_on_offer_str in ("0", "1"):

                        has_on_offer = int(has_on_offer_str)

                        product.set_has_on_offer(has_on_offer)

                        if has_on_offer == 0:

                            product.set_offer_price(0)  # Set offer price to 0

                            product.set_valid_until(None)  # Set valid until date to None

                            self.up(product, product_id)

                        elif has_on_offer == 1:

                            offer_price = input("Enter new offer price (in dollars): ")

                            valid_until = input("Enter new valid until date (yyyy-mm-dd): ")

                            product.set_offer_price(float(offer_price))

                            product.set_valid_until(valid_until)

                            self.up(product, product_id)

                        break

                    else:

                        print("Invalid input. Please enter either 0 for 'no' or 1 for 'yes'.")


            elif choice == "7":
                if product.get_has_on_offer() == 1:
                    offer_price = input("Enter new offer price (in dollars): ")
                    product.set_offer_price(float(offer_price))
                    self.up(product, product_id)
                else:
                    print("Product is not on offer. Please set 'Has on Offer' to '1' first.")
            elif choice == "8":
                if product.get_has_on_offer() == 1:
                    valid_until = input("Enter new valid until date (yyyy-mm-dd): ")
                    product.set_valid_until(valid_until)
                    self.up(product, product_id)
                else:
                    print("Product is not on offer. Please set 'Has on Offer' to '1' first.")
            elif choice == "9":
                # Finish updating
                break
            else:
                print("Invalid choice. Please select a valid option (1-9).")



    def up (self,product, product_id):

        # Update the product data in the products list
        for p in self.products:
            if p.get_product_id() == product_id:
                p.set_product_name(product.get_product_name())
                p.set_product_category(product.get_product_category())
                p.set_price(product.get_price())
                p.set_inventory(product.get_inventory())
                p.set_supplier(product.get_supplier())
                p.set_has_on_offer(product.get_has_on_offer())
                p.set_offer_price(product.get_offer_price())
                p.set_valid_until(product.get_valid_until())

        # Write the updated product data back to the 'products.txt' file
        with open("products.txt", "w") as file:
            for p in self.products:
                if p.get_has_on_offer() == 0:
                    file.write(f"{p.get_product_id()};{p.get_product_name()};{p.get_product_category()};"
                               f"{p.get_price()};{p.get_inventory()};{p.get_supplier()};{p.get_has_on_offer()}\n")
                else:
                    file.write(f"{p.get_product_id()};{p.get_product_name()};{p.get_product_category()};"
                               f"{p.get_price()};{p.get_inventory()};{p.get_supplier()};{p.get_has_on_offer()};"
                               f"{p.get_offer_price()};{p.get_valid_until()}\n")

        print("Product has been updated successfully.")

    def update_user(self):
        print("Update User :")
        user_id = input("Enter the user ID to update (6-digit integer): ")

        # Check if the user exists
        user = self.find_user_by_id(user_id)
        if user is None:
            print("User with the given ID does not exist.")
            return

        while True:
            print("Select the attribute to update:")
            print("1. User Name")
            print("2. Date of Birth")
            print("3. Role")
            print("4. Active Status")
            print("5. Finish Updating")

            choice = input("Enter your choice: ")

            if choice == "1":
                user_name = input("Enter new user name: ")
                user.set_user_name(user_name)
                self.update_user_file(user)
            elif choice == "2":
                dob = input("Enter new date of birth (dd/mm/yyyy): ")
                user.set_date_of_birth(dob)
                self.update_user_file(user)
            elif choice == "3":
                role_input = None
                while role_input is None:
                    try:
                        role_input = int(input("Enter new role (0 for admin, 1 for shopper): "))
                        role = self.validate_role(role_input)

                        if role == "admin":
                          user.set_role(0)
                        elif role == "shopper":
                            user.set_role(1)


                        print (role)
                        self.update_user_file(user)
                    except ValueError:
                        print("Invalid input. Please enter 0 for admin or 1 for shopper.")
            elif choice == "4":
                active_input = None
                while active_input is None:
                    active_input = input("Enter new active status (0 for inactive, 1 for active): ")
                    active = self.validate_active(active_input)
                    user.set_active(active)
                    self.update_user_file(user)
            elif choice == "5":
                # Finish updating
                break
            else:
                print("Invalid choice. Please select a valid option (1-5).")

        print("User information has been updated successfully.")

    def update_user_file(self, user):
        # Update the user data in the users list
        for u in self.users:
            if u.get_user_id() == user.get_user_id():
                u.set_user_name(user.get_user_name())
                u.set_date_of_birth(user.get_date_of_birth())
                u.set_role(user.get_role())
                u.set_active(user.get_active())
                u.set_basket(user.get_basket())
                u.set_order(user.get_order())

        # Write the updated user data back to the 'users.txt' file
        with open("users.txt", "w") as file:
            for u in self.users:
                basket_data = str(u.get_basket()).replace(" ", "").replace("'", "")
                if u.get_role() == 0:
                    user_data = f"{u.get_user_id()};{u.get_user_name()};{u.get_date_of_birth()};" \
                                f"admin;{u.get_active()};{basket_data};{u.get_order()}\n"
                else:
                    user_data = f"{u.get_user_id()};{u.get_user_name()};{u.get_date_of_birth()};" \
                                f"shopper;{u.get_active()};{basket_data};{u.get_order()}\n" # Define a default value if the condition is not met
                file.write(user_data)

    def list_products(self):
        while True:
            print("Choose criteria:")
            print("1. All products")
            print("2. Products with offers")
            print("3. Products by category")
            print("4. Products by name")
            print("5. Exit")

            while True:
                choice = input("Enter your choice (1/2/3/4/5): ").strip()
                if choice in ("1", "2", "3", "4", "5"):
                    break
                else:
                    print("Invalid choice. Please enter a valid number (1/2/3/4/5).")

            if choice == "1":
                self.display_all_products()
            elif choice == "2":
                self.display_products_with_offers()
            elif choice == "3":
                self.display_categories()
                category_name = input("Enter category name: ").strip()
                self.display_products_by_category(category_name)
            elif choice == "4":
                product_name = input("Enter product name: ").strip()
                self.display_products_by_name(product_name)
            elif choice == "5":
                break


    def display_all_products(self):
        for product in self.products:
            print(product.to_dict())

    def display_products_with_offers(self):
        offers = [product for product in self.products if product.get_has_on_offer() == 1]
        if not offers:
            print("No products with offers/discounts found.")
        else:
            for product in offers:
                print(product.to_dict())

    def display_categories(self):
        categories = set(product.get_product_category() for product in self.products)
        print("Available categories:")
        for category in categories:
            print(category)

    def display_products_by_category(self, category_name):
        category_products = [product for product in self.products if product.get_product_category() == category_name]
        if not category_products:
            print(f"No products found in the category '{category_name}'.")
        else:
            for product in category_products:
                print(product.to_dict())

    def display_products_by_name(self, product_name):
        name_products = [product for product in self.products if product.get_product_name() == product_name]
        if not name_products:
            print(f"No products found with the name '{product_name}'.")
        else:
            for product in name_products:
                print(product.to_dict())

    def list_all_shoppers(self):
        while True:
            print("Menu:")
            print("1. All shoppers")
            print("2. Shoppers with items in the basket")
            print("3. Shoppers with unprocessed orders")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ").strip()

            if choice == "1":
                self.display_all_shoppers()
            elif choice == "2":
                self.display_shoppers_with_items_in_basket()
            elif choice == "3":
                self.display_shoppers_with_unprocessed_orders()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid number (1/2/3/4).")

    def display_all_shoppers(self):
        shoppers = [user for user in self.users if user.get_role() == 1]
        if not shoppers:
            print("No shoppers found.")
        else:
            for shopper in shoppers:
                print(shopper.to_dict())

    def display_shoppers_with_items_in_basket(self):
        shoppers = [user for user in self.users if user.get_role() == 1 and user.get_basket()]
        if not shoppers:
            print("No shoppers with items in the basket found.")
        else:
            for shopper in shoppers:
                print(shopper.to_dict())

    def display_shoppers_with_unprocessed_orders(self):
        shoppers = [user for user in self.users if user.get_role() == 1 and user.get_order() == 1]
        if not shoppers:
            print("No shoppers with unprocessed orders found.")
        else:
            for shopper in shoppers:
                print(shopper.to_dict())



    def display_basket(self, user_id):
        # Find the user by user_id
        user = self.find_user_by_id(user_id)
        if user is None:
            print("User not found.")
            return

        # Check if the user is a shopper (role 1)
        if user.get_role() != 1:
            print("This function is available for shoppers only.")
            return

        basket = user.get_basket()
        print(basket)
        if not basket:
            print("Your basket is empty.")
            return

        total_cost = 0

        print("Products in your basket:")
        for product_id, quantity in basket.items():
            product = self.find_product_by_id(product_id)
            if product is not None:
                if product.get_has_on_offer() == 1:
                    # If the product has an offer, use offer price for cost calculation
                    cost_of_purchase = product.get_offer_price() * quantity
                else:
                    # If the product does not have an offer, use regular price for cost calculation
                    cost_of_purchase = product.get_price() * quantity

                total_cost += cost_of_purchase
                print(f"Product ID: {product_id}")
                print(f"Product Name: {product.get_product_name()}")
                print(f"Product Category: {product.get_product_category()}")
                print(f"Price: ${product.get_price()}")
                print(f"Inventory: {product.get_inventory()}")
                print(f"Supplier: {product.get_supplier()}")
                print(f"offer Price: {product.get_offer_price()}")
                print(f"Valid Until: {product.get_valid_until()}")
                print(f"Number of Items: {quantity}")
                print(f"Cost of Purchase: ${cost_of_purchase}")
                print("-" * 20)

        print(f"Total Cost of Items in Basket: ${total_cost:.2f}")

    def add_product_to_basket(self, user_id):
        # Find the user by user_id
        shopper = self.find_user_by_id(user_id)
        # Check if the user exists
        if shopper is not None :
            while True:
                # Display a list of available products
                self.display_all_products()

                product_id = input("Enter the Product ID you want to add to your basket (or 'q' to quit): ")

                # Check if the user wants to quit adding products
                if product_id.lower() == 'q':
                    break

                quantity = input("Enter the quantity of the product you want to add: ")

                # Check if the quantity is a valid integer
                try:
                    quantity = int(quantity)
                except ValueError:
                    print("Invalid quantity. Please enter a valid integer quantity.")
                    continue

                # Check if the product ID is valid
                product = self.find_product_by_id(product_id)
                if product is not None:
                    # Check if there is enough inventory
                    if quantity > 0 and product.get_inventory() >= quantity:
                        # Add the product to the shopper's basket
                        shopper.add_product_to_basket(product_id, quantity)
                        print(f"{quantity} {product.get_product_name()} added to your basket.")

                        # Update the user's information in the file
                        with open('users.txt', 'r') as file:
                            lines = file.readlines()

                        for i, line in enumerate(lines):
                            user_data = line.strip().split(';')
                            if user_data[0] == user_id:
                                # Update the user's basket in the file
                                basket_data = shopper.get_basket()
                                user_data[5] = "{" + ",".join([f'{k}:{v}' for k, v in basket_data.items()]) + "}"
                                lines[i] = ";".join(user_data) + "\n"

                        # Write the updated information back to the file
                        with open('users.txt', 'w') as file:
                            file.writelines(lines)
                    else:
                        print(f"Invalid quantity or not enough {product.get_product_name()} in stock.")
                else:
                    print("Invalid Product ID. Please choose a valid Product ID.")
        else:
            print("Invalid user ID or user is not a shopper.")

    def update_basket(self, user_id):
        # Find the user by user_id
        shopper = self.find_user_by_id(user_id)

        # Check if the user exists and is a shopper
        if shopper is not None:
            while True:
                print("Update Basket:")
                print("1. Clear Basket")
                print("2. Remove Product from Basket")
                print("3. Update Quantity of a Product in Basket")
                print("4. Exit")

                choice = input("Enter your choice (1/2/3/4): ")

                if choice == "1":
                    # Clear the shopper's basket
                    shopper.clear_basket()
                    print("Basket cleared successfully.")

                    # Update the user's information in the file
                    self.update_user_file(shopper)

                elif choice == "2":
                    # Display the shopper's current basket
                    self.display_basket(user_id)

                    product_id = input("Enter the Product ID to remove from the basket (or 'q' to quit): ")

                    # Check if the user wants to quit
                    if product_id.lower() == 'q':
                        continue

                    # Check if the product ID is valid
                    if not self.find_product_by_id(product_id):
                        print("Invalid Product ID. Please choose a valid Product ID.")
                        continue

                    # Remove the specified product from the basket
                    if shopper.remove_product_from_basket(product_id):
                        print(f"Product with ID {product_id} removed from the basket successfully.")
                    else:
                        print(f"Product with ID {product_id} was not found in the basket.")

                    # Update the user's information in the file
                    self.update_user_file(shopper)

                elif choice == "3":
                    # Display the shopper's current basket
                    self.display_basket(user_id)

                    product_id = input("Enter the Product ID to update quantity (or 'q' to quit): ")

                    # Check if the user wants to quit
                    if product_id.lower() == 'q':
                        continue

                    # Check if the product ID is valid
                    product = self.find_product_by_id(product_id)
                    if not product:
                        print("Invalid Product ID. Please choose a valid Product ID.")
                        continue

                    # Prompt for the new quantity
                    new_quantity = input("Enter the new quantity: ")

                    try:
                        new_quantity = int(new_quantity)
                        if new_quantity >= 0:
                            # Check if the new quantity exceeds available inventory
                            if new_quantity <= product.get_inventory():
                                # Update the quantity of the specified product in the basket
                                if shopper.update_product_quantity_in_basket(product_id, new_quantity):
                                    print(f"Quantity of Product with ID {product_id} updated successfully.")
                                else:
                                    print(f"Product with ID {product_id} was not found in the basket.")

                                # Update the user's information in the file
                                self.update_user_file(shopper)
                            else:
                                print("New quantity exceeds available inventory. Please enter a valid quantity.")
                        else:
                            print("Invalid input. Please enter a non-negative integer for quantity.")
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric quantity.")

                elif choice == "4":
                    # Exit the update basket menu
                    break
                else:
                    print("Invalid choice. Please select a valid option (1/2/3/4).")

    def place_order(self, user_id):
        # Find the user by user_id
        shopper = self.find_user_by_id(user_id)

        # Check if the user exists and is a shopper
        if shopper is not None and shopper.get_role() == 1:
            if shopper.get_order() == 1:
                print("Your order is already placed.")
            else:
                # Request the purchase of items by changing the order field to 1
                shopper.set_order(1)

                # Update the user's information in the in-memory list
                for user in self.users:
                    if user.get_user_id() == user_id:
                        user.set_order(1)

                # Update the user's information in the 'users.txt' file
                with open('users.txt', 'r') as file:
                    lines = file.readlines()

                for i, line in enumerate(lines):
                    user_data = line.strip().split(';')
                    if user_data[0] == user_id:
                        user_data[-1] = '1'  # Set the order field to 1
                        lines[i] = ";".join(user_data) + "\n"

                # Write the updated information back to the file
                with open('users.txt', 'w') as file:
                    file.writelines(lines)

                print("Your order has been placed successfully.")
        else:
            print("Invalid user ID or user is not a shopper.")

    def execute_order(self, admin_id):
        # Find the admin user by admin_id
        admin = self.find_user_by_id(admin_id)

        # Check if the user exists and is an admin
        if admin is not None :
            while True:
                print("Execute Order Menu:")
                print("1. List Shoppers with Unprocessed Orders")
                print("2. Execute Order for a Shopper")
                print("3. Exit")

                choice = input("Enter your choice (1/2/3): ")

                if choice == "1":
                    # List shoppers with unprocessed orders
                    shoppers_with_orders = [
                        user for user in self.users if user.get_role() == 1 and user.get_order() == 1
                    ]
                    if not shoppers_with_orders:
                        print("No shoppers with unprocessed orders found.")
                    else:
                        print("Shoppers with Unprocessed Orders:")
                        for i, shopper in enumerate(shoppers_with_orders, start=1):
                            print(f"{i}. User ID: {shopper.get_user_id()}, User Name: {shopper.get_user_name()}")

                elif choice == "2":
                    # Execute order for a selected shopper
                    shopper_id = input("Enter the User ID of the shopper to execute their order (or 'q' to quit): ")
                    if shopper_id.lower() == 'q':
                        continue

                    shopper_to_execute = self.find_user_by_id(shopper_id)

                    if shopper_to_execute is not None:
                        if shopper_to_execute.get_role() == 1:
                            if shopper_to_execute.get_order() == 1:
                                # Execute the order: Deduct items from product inventory and clear the basket
                                basket = shopper_to_execute.get_basket()
                                order_accepted = True  # Assume order is accepted by default
                                order_rejected_reason = ""

                                for product_id, quantity in basket.items():
                                    product = self.find_product_by_id(product_id)
                                    if product is not None:
                                        if product.get_inventory() >= quantity:
                                            product.set_inventory(product.get_inventory() - quantity)
                                        else:
                                            # Insufficient inventory for this product
                                            order_accepted = False
                                            order_rejected_reason = f"Insufficient inventory for product ID {product_id}"
                                            break  # Exit the loop early

                                if order_accepted:
                                    self.update_products_file(basket)
                                    # Clear the shopper's basket and update order status
                                    shopper_to_execute.clear_basket()
                                    shopper_to_execute.set_order(0)

                                    # Update user and product information
                                    self.update_user_file(shopper_to_execute)


                                    print("Order executed successfully.")
                                else:
                                    # Order is not accepted
                                    print(f"Order not accepted: {order_rejected_reason}")
                                    # Write the user ID and notification to notifications.txt
                                    with open("notifications.txt", "a") as notifications_file:
                                        notifications_file.write(
                                            f"User ID: {shopper_to_execute.get_user_id()}, Notification: Order not accepted - {order_rejected_reason}\n")

                            else:
                                print("The selected shopper does not have an unprocessed order.")
                        else:
                            print("The selected user is not a shopper.")
                    else:
                        print("Invalid shopper User ID.")
                elif choice == "3":
                    # Exit the execute order menu
                    break
                else:
                    print("Invalid choice. Please select a valid option (1/2/3).")

    def check_notifications(self, user_id):
        try:
            with open("notifications.txt", "r") as notifications_file:
                lines = notifications_file.readlines()

            found_notification = False
            with open("notifications.txt", "w") as notifications_file:
                for line in lines:
                    if f"User ID: {user_id}" in line:
                        print("You have a notification about your last order: ")
                        print(line.strip())
                        found_notification = True
                    else:
                        notifications_file.write(line)


        except FileNotFoundError:
            print("The notifications file does not exist.")


    def update_products_file(self, basket):
            # Implement the logic to update the products file here
            # This method should update the product inventory based on the items in the basket

            for product_id, quantity in basket.items():
                product = self.find_product_by_id(product_id)
                if product is not None:
                    if product.get_inventory() >= quantity:
                        product.set_inventory(product.get_inventory() - quantity)
                    else:
                        # Insufficient inventory for this product
                        print(f"Insufficient inventory for product ID {product_id}")

            # After updating the product inventory, write the updated product information to the products file
            with open("products.txt", "w") as products_file:
                for product in self.products:
                    # Write product information to the file
                    if product.get_has_on_offer() == 1:
                        product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                       f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()};{product.get_offer_price()};{product.get_valid_until()}\n"
                    else:
                        product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                       f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()}\n"
                    products_file.write(product_data)





if __name__ == "__main__":
    ecommerce_system = ECommerceSystem()
    ecommerce_system.run()



