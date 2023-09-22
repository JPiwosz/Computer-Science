my_sportlist = ["Football", "Basketball"]
favouritesport = input("What is your favourite sport ? ")
my_sportlist.append(favouritesport)
my_sportlist.sort()
print(my_sportlist)


schoolsubjects = ["science", "computer science","maths","biology","economics"]
print(schoolsubjects)
dislikedsubject = input("which of these subjects do you dislike ? ")
schoolsubjects.remove(dislikedsubject)
print("Your New list is",schoolsubjects)


colourlist = ["blue","red","yellow","white","green","black","purple","brown","grey","neon"]
number1 = input("Please pick an starting number between 0 - 4  ")
number2 = input ("Please pick an end number between 5 - 9  ")
number1= int(number1)
number2 =int(number2)
print(colourlist[number1:number2])
print(colourlist[number1])
print(colourlist[number2])


numberlist = ["123","456","789"]
for item in numberlist:
    print(item)
threedigetnumber = 