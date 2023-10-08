Direction = input("Select an direction up or down ?  ")
if Direction == "up":
    print("I do not understand")
    topnumber = input("Please type the top number  ")
    newtopnumber = int(topnumber)
    startnumber = 1
    while startnumber != newtopnumber +1:
        print(startnumber)
        startnumber = startnumber + 1
if Direction != "up" or  Direction != "down":
    print("I do not understand")
if Direction == "down":
    bottemnumber = input("Please enter a number less than 20  ")
    bottemnumberint = int(bottemnumber)
    if bottemnumberint < 20:
         while bottemnumberint != 20 +1:
             print(bottemnumberint)
             bottemnumberint = bottemnumberint +1

             
userinv = input("How many people do you want to invite to the party  ")
userinvint = int(userinv)
if userinvint < 10:
    for i in range(userinvint):
        nameofperson = input("Please enter their name   ")
        print(nameofperson,"Has been invited")
if userinvint >= 10:
    print("Too many people")
    
    