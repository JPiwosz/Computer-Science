
             

comp_num = highlow(high,low)
print(comp_num)
randombetween = randomnum()
print(randombetween)
asd = guessing(comp_num,randombetween)
if asd == 1:
    print("You win")
while asd == 2:
    print("Wrong")
    if comp_num < randombetween:
        guesslower = input("Your guess was too high, guess lower    ")
        randombetween = int(guesslower)
        
    if comp_num > randombetween:
        guesshigher = input("Your guess was too low, guess higher   ")
        randombetween = int(guesshigher)
        
    if comp_num == randombetween :
        print("You win")
        break

import random

def choice1():
    random1 = random.randint(5,20)
    random2 = random.randint(5,20)
    random1str = str(random1)
    random2str = str(random2)
    useranswer = input("Whats" + " " + random1str  + " + " + random2str  + " ?  ")
    print(useranswer)
    correctanswer = random1 + random2
    print("The correct answer is",correctanswer,)
    return [int(useranswer),int(correctanswer)]
    
def choice2():
    random1 = random.randint(25,50)
    random2 = random.randint(1,25)
    random1str = str(random1)
    random2str = str(random2)
    useranswer = input("Whats" + " " + random1str + " - " + random2str + " ?  ")
    correctanswer = random1 - random2
    print("The correct asnwer is",correctanswer,)
    return [int(useranswer),int(correctanswer)]
    

def corrections(useranswer,correctanswer):
    if useranswer == correctanswer:
        print("Correct")
    if useranswer != correctanswer:
        print("Incorrect","the answer is",correctanswer)

menu = "1) Addition \n2) Subtraction "
print(menu)
menuinput = input("Enter 1 or 2:   ")

if not menuinput.isdigit():
    print("IT WAS SO SIMPLE ALL I NEEDED YOU TO DO IS CHOOSE BETWEEN 1 OR 2 NOT ANY OTHER NUMBER YOU ABSOLUTE BAFOON!!!!")
    
elif int(menuinput) > 2 or int(menuinput)<1:
    print("IT WAS SO SIMPLE ALL I NEEDED YOU TO DO IS CHOOSE BETWEEN 1 OR 2 NOT ANY OTHER NUMBER YOU ABSOLUTE BAFOON!!!!")
else:
    menuinputint = int(menuinput)
    print(menuinput)
    menuinput = int(menuinput)

if menuinput == 1:
    A =choice1()
    corrections(A[0],A[1])
    
if menuinput == 2:
    B = choice2()
    corrections(B[0],B[1])
"""


namelist = []

def choice1(namelist):
    addname = input("Enter The Name You Want To Add To The List   ")
    namelist.append(addname)
    print(namelist)
    return(namelist)
    
def choice2(namelist):
    print(namelist)
    deletename = input("Enter The Name You Want To Delete From The List   ")
    print(namelist)
    indexpos = namelist.index(deletename)
    print(indexpos)
    del namelist[indexpos]
    return(namelist)

def choice3(namelist):
    changename = input("Enter the name you wish to change   ")
    indexpos1 = namelist.index(changename)
    print(indexpos1)
    del namelist[indexpos1]
    
    changedname = input("Enter what you want to change that name to   ")
    namelist.insert(indexpos1,changedname)
    return(namelist)

def choice4(namelist):
    displaylist = namelist
    print(displaylist)
    return(namelist)

def menu():
        menu1 = "1) Add a Name \n2) Delete a Name \n3) Change a Name \n4) View All Names In The List \n5) End The Program"
        print(menu1)
        menuchoice = input("Select ->   ")
        print(menuchoice)
    
        if not menuchoice.isdigit():
            print("Selected Number was not between 1 and 5")
    
        elif int(menuchoice) < 1 or int(menuchoice) > 5:
            print("Selcted Number was not between 1 and 5")
        else:
            menuchoiceint = int(menuchoice)
        return menuchoiceint


menuchoice = menu()  
while menuchoice != 5:
    if int(menuchoice) == 1:
        A = choice1(namelist)
    if int(menuchoice) == 2:
        B = choice2(namelist)
    if int(menuchoice) == 3:
        C = choice3(namelist)
    if int(menuchoice) == 4:
        D = choice4(namelist)
    menuchoice = menu()  

    

    
        
    
    
    


    
    



































