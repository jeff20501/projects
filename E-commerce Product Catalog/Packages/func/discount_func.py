#discount_func
def discounts():
    print("To apply a discount to the product follow the instructions below:")
    global price
    global discount
    try: 
        price = float(input("Enter the price of the product: "))
        discount = float(input("Enter the discount you want to apply to this product(Give the discount as a percentage)"))
    except ValueError:
        print("Enter a number for the price and discounts!!")
        
def discounts_calc():
    if price > 3000:
        result = 100 - discount
        new_price = result * price / 100
        return new_price
    else:
        print(f"The price for the product {price} is too small to be applied a discount!!")
        