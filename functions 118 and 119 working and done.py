
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

        

    
