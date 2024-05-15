"""
nlist = []
for i in range(5):
    nuser = input("Enter a number for the list  ")
    nlist.append(nuser)
print(nlist)
for i in range(len(nlist)):
    nlist[i] = int(nlist[i]) + 1
print(nlist)


Hours = [12,7,9,9,6,8,2]
cost_liter = 1.35
total_liters = sum(Hours)
total_liters = total_liters*0.5
print("Total Amount of liters is",total_liters)
pricetotal = total_liters * cost_liter
pricetotal = round(pricetotal,2)
print("The price of the milk in a week is",pricetotal,"€")
"""

print("RainFall Program")
print("You will be asked to enter the day of the week and the rainfall on that day")
week = ["Monday","Tuesday","Wensday","Thursday","Friday","Saturday","Sunday"]
total_rainfall = 0
for i in week:
    rainfall = input("enter the amount of rainfall on " +i+ " in cm  ")
    total_rainfall = total_rainfall + float(rainfall)
    total_rainfall = round(total_rainfall,2)
    print("The total amount of rainfall this week is",total_rainfall,"cm")
    
    
    
    