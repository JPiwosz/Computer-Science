takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00
TotalValue = 0
pos = 1
total_list = []

print("Welcome to the takeaway delivery service.")
Name = input("Please enter your name: ")
print("Here's our menu.")
for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase? "))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
print("Thank you,",Name," your order is as follows")
for item in order:
    print(takeaway_menu[item-1])
    
for i in order:
    pos = i
    pos = pos -1
    value1 = takeaway_prices[pos]
    total_list.append(value1)
    TotalValue = sum(total_list)
    
"""    
if TotalValue > 30:
    print("free delivery")
    TotalValue = TotalValue - delivery_fee
    TotalV = round(TotalValue,ndigits=2)
    print("Your total recipt is,",TotalV)
        
if TotalValue < 30:
    print("Delivery Fee of 5$")
    TotalValue = TotalValue + delivery_fee
    TotalV = round(TotalValue,ndigits=2)
    print("Your total recipt is,",TotalV)
"""

def get_bill_total(TotalValue):
    if TotalValue > 30:
        print("free delivery")
        TotalValue = TotalValue - 5
        TotalV = round(TotalValue,ndigits=2)
        print("Your total recipt is,",TotalV,"$")
    if TotalValue < 30:
        print("Delivery Fee of 5$")
        TotalValue = TotalValue + 5
        TotalV = round(TotalValue,ndigits=2)
        print("Your total recipt is,",TotalV,"$")
    return TotalV

Recipt = get_bill_total(TotalValue)



