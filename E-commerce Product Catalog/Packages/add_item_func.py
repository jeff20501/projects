def add_item_func():
    new_item_name = input("Enter the name of the product you want to add: ")
    new_item_product_id = input("Enter the product ID of the product: ")
    new_item_price = int(input("Enter the price of the product: "))
    return new_item_name, new_item_price, new_item_product_id

def add_ele():
    #call the func add_item_func once and store it's return values
    item_name, item_price, item_product_id = add_item_func()
    new_item_warranty = int(input("Enter the warranty of the product: "))
    return new_item_warranty, item_name, item_price, item_product_id

def add_clo():
    item_name, item_price, item_product_id = add_item_func()
    new_item_size = input("Enter the size of the clothing: ")
    new_item_material = input("Enter the material used to make the clothing: ")
    return new_item_size, new_item_material, item_name, item_price, item_product_id

    