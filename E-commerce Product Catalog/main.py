#main
from Packages.menu import main_menu, electronics_menu, clothing_menu, add_product_menu
from Packages.classes import Product, Electronics, Clothing, Catalog
from func.discount_func import discounts
from Packages.add_item_func import add_ele, add_clo

def main():
    electronics_list = [
        Electronics(name='Samsung [Soundbar] J series', price=50000, product_id='E100f22z', warranty_period=24),
        Electronics(name='HP Elitebook 840 G6', price=48000, product_id='P100ez840', warranty_period=6),
        Electronics(name='Samsung S23', price=124000, product_id="SA100yex24", warranty_period=24)
    ]
    
    clothing_list = [
        Clothing(name='Hoodie', price=500, product_id='10004rd', size='XXXL', material='cotton'),
        Clothing(name='Nike J4', price=4500,product_id='254ERD5CFDS', size='41', material='Leather and cotton'),
        Clothing(name='Cargo pants', price=300, product_id='E101jkia45', size='XXL', material='cotton')
    ]
    
    items = Catalog()
    
    while True:
        main_menu()
        try: 
            choice = int(input("Where do you want to go: "))
            if choice == 1:
                electronics_menu()
                try:
                    choice_electronics= int(input("Enter the action you want to do to this class: "))
                    if choice_electronics == 1:
                        print("To know the warranty of the product kindly follow the following:")
                        name_product_warranty=input("Enter the name of the product you want to know it's warranty: ")
                        productid_warranty = input("Enter the product id of the product: ")
                        product_found = False  # To track if the product is found
                        for pro in electronics_list:
                            if pro.name == name_product_warranty:
                                if pro.product_id == productid_warranty:
                                    pro.know_warranty_period(name_product_warranty, productid_warranty)
                                    product_found = True  # The product was found and the warranty period is checked
                                    break  # Exit the loop since we found the matching product
                                else:
                                    print("The product ID given is incorrect try again!!")
                                    product_found = True # Product was found by name but with wrong product_id
                                    break
                        if not product_found:
                            print(f"The product with the name: {name_product_warranty} can not be found.")
                    
                    elif choice_electronics == 2:
                        name_product_apply_discount= input("Enter the name of the product you want to apply the discount to: ")  
                        for ele in electronics_list:
                            if ele.name == name_product_apply_discount:
                                if ele.price > 3000:
                                    discounts()
                                    ele.apply_discounts()
                                else: 
                                    print("The price of the product is too slow to apply any discount!!")
                            else:
                                print("The product with the name given can not be located at this moment!!") 
                    
                    elif choice_electronics == 3:
                        for ele in electronics_list:
                            ele.display_product_details()
                            print()
                            if not ele:
                                print("There are currently no electronics Product at this time.")
                    
                    elif choice_electronics == 4:
                        print("Thank you for choosing us! See you next time BROO!!")
                        break
                    
                    else:
                        print("Invalid input! Enter either 1,2,3,4 or 5 to exit. Try again!")
                        
                except ValueError:
                    print("Enter a number as an option as shown by the choices!!")
            
            elif choice == 2:
                clothing_menu()
                try:
                    choice_clothing = int(input("Enter the action you want to do to this class: "))
                    if choice_clothing ==  1:
                        print("To know the size of the clothing follow the below instructions.")
                        name_product_know_size = input("Enter the name of the clothing you want to know it's size: ")
                        product_found = False
                        for clo in clothing_list:
                            if clo.name == name_product_know_size:
                                clo.know_size(name_product_know_size)
                                product_found = True
                                break
                            else:
                                print("The name of the clothing you gave can't be located at this time try again next time!!")
                    
                    elif choice_clothing == 2:
                        print("To know the the material used to make the clothing follow the below instructions.")
                        name_product_know_material = input("Enter the name of the clothing you want to know the material it's made off: ")
                        product_found=False
                        for clo in clothing_list:
                            if clo.name == name_product_know_material:
                                clo.know_material(name_product_know_material)
                                product_found=True
                                break
                            else:
                                print("The product with the product name you gave can not be located at this momoent try again next time!!")
                    
                    elif choice_clothing == 3:
                        name_product_apply_discount_clo= input("Enter the name of the product you want to apply the discount to: ")
                        product_found=False
                        for pro in electronics_list:
                            if pro.name == name_product_apply_discount_clo:
                                if pro.price > 3000:
                                    discounts()
                                    pro.apply_discounts()
                                    product_found=True
                                    break
                                else: 
                                    print("The price of the product is too small to apply any discount!!")
                        if not product_found:
                            print("The product with the name given can not be located at this moment!!")
                    
                    elif choice_clothing == 4:
                        for clo in clothing_list:
                            clo.display_product_details()
                            if not clo:
                                print("There is currently no clothing in this shop at this momoent try again later!!")
                    
                    elif choice_clothing == 5:
                        print("Thank you for choosing us. See you next time!!")
                    
                    else:
                        print("Invalid input! Enter either 1,2,3,4 or 5 to exit. Try again!")                                            
                
                except ValueError:
                    print("Enter a number as an option as shown by the choices!!")
            
            elif choice == 3:
                add_product_menu()
                choice_add_item = int(input("Enter the choice you want to do: "))
                if choice_add_item == 1:
                    new_item_warranty, item_name, item_price, item_product_id = add_ele()
                    new_ele = Electronics(item_name, item_price, item_product_id, new_item_warranty)
                    items.adding_products(new_ele)
                
                elif choice_add_item == 2:
                    new_item_size, new_item_material, item_name, item_price, item_product_id = add_clo()
                    new_clo = Clothing(item_name, item_price, item_product_id, new_item_size, new_item_material)
                    items.adding_products(new_clo)
                else:
                    print("U are leaving this page! Goodbye!!")
                    break
                    
            elif choice == 4:
                   name_product_apply_discount_catalog = input("Enter the name if th product you want to apply a discount to: ")
                   product_found=False
                   for item in items.catalog:
                        if item.name == name_product_apply_discount_catalog:
                           if item.price > 3000:
                               discounts()
                               item.apply_discounts()
                               product_found=True
                               break
                           else:
                               print("The price of the product is too small to be applied a discount!!")
                   if not product_found: 
                        print(f"The product with the name: {name_product_apply_discount_catalog} Can not be located in our catalog!! Try again!")
            
            elif choice == 5:
                items.listing_all_products()
                print()
            
            elif choice == 6:
                print("Thank you for choicing us goodbye!!")
                break
            
            else:
                print("Invalid input! Enter either 1,2,3,4,5 or 6 to exit.")                        
                                
        
        except ValueError:
            print("Enter a number as an option as shown by the choices!!")

if __name__ == "__main__":
    main()        
                           