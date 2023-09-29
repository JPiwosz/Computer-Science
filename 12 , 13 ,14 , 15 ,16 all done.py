
TvList = ["Stranger Things","Breaking Bad","Family Guy"]
for variable in TvList:
    print(variable)
Extrashow = input("Name another Tv show that will be added to this list please  ")
#Extrashow = list(Extrashow)
print(Extrashow)
TvList.append(Extrashow)
print("Your New list of Shows is")
for every_item in TvList:
    print(every_item, end="\n")
    
    

number1 = input("Please give me any number  ")
number2 = input("Please give me another number  ")
newnumber1 = int(number1)
newnumber2 = int(number2)
if newnumber1 > newnumber2:
    print(newnumber2,newnumber1)
if newnumber1 < newnumber2:
    print(newnumber1,newnumber2)
    
number3 = input("Please enter a number that is less then the value of 20  ")
newnumber3 = int(number3)
if newnumber3 < int(20) :
    print("Thank you")
if newnumber3 > int(20):
    print("Too High")
    
number4 = input("Please enter a number that is between the value of 10 and 20  ")
newnumber4 = int(number4)
if newnumber4 <= 20 and newnumber4 >= 10:
    print("Thank you")
else:
    print("Inncorect Value")
    

favouritecolour = input("Please Enter Your Favourite Colour!  ")
if favouritecolour == "RED" or favouritecolour == "red":
    print("I like the colour red too :) ")
if favouritecolour != "RED" or favouritecolour != "red":
    print(favouritecolour)
   
weather = input("Is it raining right now ?  ")
weather1 = weather.lower()
print(weather1)
if weather1 == "yes":
    windy = input("Is it windy right now ?  ")
    windyNew = windy.lower()
    if windyNew == "yes":
        print("It is too windy for an Umbrella")
    else:
        if windyNew == "no":
            print("Take an Umbrella")