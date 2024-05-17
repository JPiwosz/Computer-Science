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


print("RainFall Program")
print("You will be asked to enter the day of the week and the rainfall on that day")
week = ["Monday","Tuesday","Wensday","Thursday","Friday","Saturday","Sunday"]
av = []
total_rainfall = 0
for i in week:
    rainfall = input("enter the amount of rainfall on " +i+ " in cm  ")
    if float(rainfall) > 3.5:
        print("working")
        exceed = float(rainfall) - 3.5
        exceed = round(exceed,2)
        print("It exceeded 3.5cm of rainfall by,",exceed,"cm on",i)
    total_rainfall = total_rainfall + float(rainfall)
    av.append(float(rainfall))
    total_rainfall = round(total_rainfall,2)
print("The total amount of rainfall this week is",total_rainfall,"cm")
averadge = sum(av)
averadge = averadge / 2
print("The averadge amount rainfall this week is",averadge,"cm")
"""

menu = "***WELCOME*** \n\nPlease choose an option below\n\n1. Enter sales data\n2. View total sales to date\n3. View maxinum sale value of any staff member\n4. View minimum sale of any staff member\n5. View adveradge sale value of any staff member\n6. Enter -1 to end this program"
print(menu)
option = 0
value = 0
maxinum = 0
values = []
names = []

while option != 6:
    option = input("\n---->  ")
    if int(option) == 1:
        name = input("Enter the name of the sales person\n---> ")
        valueI = input("Enter the value of their sale\n---> ")
        values.append(int(valueI))
        names.append(name)
    
    if int(option) == 2:
        for i in range(len(values)):
            valuestore = values[i]
            value = int(value) + int(valuestore)
        print("The total value of sales made to date is,",value,"€")
        
    if int(option) == 3:
        staffname = input("Enter the name of the staff member\n--> ")
        count = names.count(staffname)
        print(count)
        for i in range(count):
            


    

    

    
    