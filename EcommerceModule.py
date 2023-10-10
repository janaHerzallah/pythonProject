# this module is to manage writing to file processes

def save_products_to_file(product_list, filename):
    try:
        with open(filename, 'w') as products_file:
            for product in product_list:
                if product.get_has_on_offer() == 1:
                    product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                   f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()};{product.get_offer_price()};{product.get_valid_until()}\n"
                else:
                    product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                   f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()}\n"
                products_file.write(product_data)
        print(f"Products have been successfully saved to {filename}")
    except IOError:
        print("Error: Unable to write to the file")

        def save_products_to_file(product_list, filename):
            try:
                with open(filename, 'w') as products_file:
                    for product in product_list:
                        if product.get_has_on_offer() == 1:
                            product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                           f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()};{product.get_offer_price()};{product.get_valid_until()}\n"
                        else:
                            product_data = f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_price()};" \
                                           f"{product.get_inventory()};{product.get_supplier()};{product.get_has_on_offer()}\n"
                        products_file.write(product_data)
                print(f"Products have been successfully saved to {filename}")
            except IOError:
                print("Error: Unable to write to the file")


def save_users_to_file(users_list, filename):
    try:
        with open(filename, "a") as file:
            for user in users_list:
                user_data = f"{user.get_user_id()};{user.get_user_name()};{user.get_date_of_birth()};" \
                            f"{user.get_role()};{user.get_active()};{user.get_basket()};{user.get_order()}\n"
                file.write(user_data)
        print(f"Users have been successfully saved to {filename}")
    except IOError:
        print("Error: Unable to write to the file")