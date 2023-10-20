
import random

myNum = random.randrange(0,100)
print(myNum)

myChoice = random.choice(["apple","banana","starwberry","mango","grape"])
print(myChoice)

flipcoin = random.choice(["heads","tails"])
usercoin = input("Please choose a side of the coin heads or tails??    ")
if usercoin == flipcoin:
    print("You Win!!")
elif usercoin != flipcoin:
    print("Bad luck try again")
   
randomnum = random.randrange(1,5)
usernum = input("Please pick a number between 1 and 5   ")
randomnumint  = int(randomnum)
usernumint = int(usernum)
if usernumint == randomnumint:
    print("Well done!")
elif usernumint != randomnumint:
    if usernumint > randomnumint:
        print("too high")
    elif usernumint < randomnumint:
        print("too low")
    secondchance = input("try again   ")
    secondchanceint = int(secondchance)
    if secondchanceint == randomnumint:
        print("Correct")
    elif secondchance != randomnumint:
        print("you loose")


randomwholenum = random.randrange(1,10)
userguess = input("Please enter a number between 1 and 10   ")
randomwholenumint = int(randomwholenum)
userguessint = int(userguess)
if userguessint == randomwholenumint:
    print("You win")
while userguessint != randomwholenumint:
    if userguessint > randomwholenumint:
        print("too high")
    elif userguessint < randomwholenumint:
        print("too low")
    userguess = input("Please enter a number between 1 and 10   ")
    userguessint = int(userguess)
    if userguessint == randomwholenumint:
        print("You got it!")
        break

score = 0
print("Maths Quiz")
for i in range(5):
    num1 = random.randrange(1,100)
    num2 = random.randrange(1,100)
    num1str = str(num1)
    num2str = str(num2)
    question = input("whats " + num1str + " + " + num2str +  " ?   ")
    num1int = int(num1)
    num2int = int(num2)
    sum = num1int + num2int
    answer = int(question)
    if answer == sum:
        print("Correct!!!")
        score = score + 1
    elif answer != sum:
        print("Wrong!")
print("Maths Quiz Complete")
print("Your final score out of 5 is", score)


colours = random.choice(["red","green","blue","yellow","black"])
print(colours)
usercolour = input("Please pick an colour    ")
if usercolour == colours:
    print("Well Done!")
elif usercolour != colours:
    print("Your poo is",colours)
guessagain = input("Guess Again   ")
