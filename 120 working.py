"""
def number():
    X = input("Please enter any number   ")
    num = int(X)
    return num
plumber = number()


one = 1

def countB(one,number):
    while one < number:
        print(one)
        one = one + 1
    return one
print(countB(one,plumber))

import random
high = input("Please enter a high number   ")
high = int(high)
low = input("Please enter a low number    ")
low = int(low)

def highlow(highV,lowV):
    randomvalue = random.randint(lowV,highV)
    return randomvalue

def randomnum():
    print("I am thinking of a number")
    guess = input("Guess the number I am thinking of   ")
    return int(guess)

def guessing(comp_num,guess):
    if comp_num == guess:
        return 1
    else:
        return 2
        
             

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
"""
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
