#Classes
from func.discount_func import discounts_calc
class Product:
    def __init__(self,name, price, product_id):
        self.name=name
        self.price=price
        self.product_id=product_id
    
    def display_product_details(self):
        raise NotImplementedError("Each subclass needs to implement this method")
    
    def apply_discounts(self):
        raise NotImplementedError("Each subclass needs to implement this method")
    
class Electronics(Product):
    def __init__(self, name, price , product_id, warranty_period):
        super().__init__(name, price, product_id)
        self.warranty_period=warranty_period
    
    def know_warranty_period(self, name, product_id):
        print(f"The product NAME: {self.name} Product ID: {self.product_id} Warranty : {self.warranty_period}")
    
    def apply_discounts(self):
        discount = float(input("Enter the discount you want to apply to this product(Give the discount as a percentage)"))
        new_price = discounts_calc(self.price, discount)
        print(f"The product Name: {self.name} Price: {self.price}. The price after discount is applied: {new_price}")
        new_price = self.price
    
    def display_product_details(self):
        print(f" Name: {self.name} Price: {self.price} Product ID: {self.product_id} Warranty Period : {self.warranty_period}")
        print()
    
class Clothing(Product):
    def __init__(self, name, price, product_id, size, material):
        super().__init__(name, price, product_id)
        self.size=size
        self.material=material
    
    def know_size(self, name):
        print(f"The prouct Name: {self.name} Size: {self.size}")
        
    def know_material(self, name):
        print(f"The product Nmae: {self.name} Material: {self.material}")
        
    def apply_discounts(self):
        discount = float(input("Enter the discount you want to apply to this product(Give the discount as a percentage)"))
        new_price = discounts_calc(self.price, discount)
        print(f"The product Name: {self.name} Price: {self.price}. The price after discount is applied: {new_price}")
        new_price = self.price
    
    def display_product_details(self):
        print(f" Name: {self.name} Price: {self.price} Product ID: {self.product_id} Warranty Period : {self.warranty_period}")
        print()
        
class Catalog:
    def __init__(self):
        self.catalog = []
    
    def adding_products(self, product):
        self.catalog.append(product)
        print(f"The product Name: {product.name} Product ID: {product.product_id} Price: {product.price}")
    
    def apply_discounts(self, discount):
        for pro in self.catalog:
            pro.apply_discount()
    
    def  listing_all_products(self):
        for pro in self.catalog:
            pro.display_product_details()