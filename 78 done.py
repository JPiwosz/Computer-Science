TvList = ["Stranger Things","Breaking Bad","Family Guy"]
for variable in TvList:
    print(variable)
Extrashow = input("Name another Tv show that will be added to this list please  ")
#Extrashow = list(Extrashow)
print(Extrashow)
TvList.append(Extrashow)
for every_item in TvList:
    print(every_item, end="\n")

