quantity = float(input("Enter quantity of good you purchased: "))

print("Quantity of product u purchased is: ", quantity)

"""
unitry method:
 1 quantity product = 100 bucks
 x quantity product = x * 100 bucks
"""
purchased_cost = quantity*100 # cost of purchased product
cost_afterDiscount = 0  # discounted 
if purchased_cost > 1000:
    print(f' ur actuall cost is: {purchased_cost} bucks')

    print("Congrats u r eligible for '10%' discount!!!")

    cost_afterDiscount = purchased_cost - (purchased_cost * 0.1) 
    print(f" Price u have to pay after '10%' discount is: {cost_afterDiscount} bucks")

else:
    print(f"unfortunately!!! u r not eligible for discount")










































