print("RainFall Program")
print("You will be asked to enter the day of the week and the rainfall on that day")
week = ["Monday","Tuesday","Wensday","Thursday","Friday","Saturday","Sunday"]
av = []
tracker = 0 # This tracks the index position of the rainfall so we can get the corresponding day 
exceed = 0
total_rainfall = 0
for i in week:
    rainfall = input("enter the amount of rainfall on " +i+ " in cm  ")
    total_rainfall = total_rainfall + float(rainfall)
    av.append(float(rainfall))
    total_rainfall = round(total_rainfall,2)
print("The total amount of rainfall this week is",total_rainfall,"cm")
averadge = sum(av)
averadge = averadge / 2
print("The averadge amount rainfall this week is",averadge,"cm")

for x in av:
    if x > 3.5:
        day_tracker = week[tracker]
        exceed = x - 3.5
        exceed = round(exceed,2)
        print("It exceeded 3.5cm of rainfall by,",exceed,"cm on",day_tracker)
    tracker = tracker +1