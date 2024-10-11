#discount_func
def discounts_calc(price, discount):
    # Function to calculate the discounted price.
    if price > 3000:
        result = price - (price * (discount / 100))
        return result
    else:
        print(f"The price for the product {price} is too small to be applied a discount!!")
        return price #return the original price

