
start = 0
total = start
print(total)
while total <=  50:
    numberadd = input("Please enter an input to be added to the total   ")
    numberaddint = int(numberadd)
    total = total + numberaddint
    print("The total is",total)
    

usernum = input("Please enter an number   ")
usernumint = int(usernum)
while usernumint < 5:
    ask = input("Please enter an number   ")
    askint = int(ask)
    if askint > 5:
        print("The last number you entered was",askint)
        break


num1 = input("Please enter an number   ")
num2 = input("Please enter another number   ")
num1 = int(num1)
num2 = int(num2)
print(num1,num2)
numbers = num1 + num2
print(numbers)
anothernumber = input("Do you want to add another number? ansewer with y or n   ")
while anothernumber == "y":
    anothernum = input("Please enter another number that will be added   ")
    anothernum = int(anothernum)
    numbersnew = numbers + anothernum
    print(numbers)
    anothernumber = input("Do you want to add another number? ansewer with y or n   ")


invite = input("Please enter the name of someone you want to invite to the party   ")
print(invite)
count = 0
print(invite,"Has been invited")
count = count + 1
somelse = input("Do you wish to invite somebody else answer with either y or n    ")
while somelse == "y":
    invite = input("Please enter the name of someone you want to invite to the party   ")
    count = count + 1
    somelse = input("Do you wish to invite somebody else answer with either y or n    ")
print(count,"people have been invited")

compnum = 50
print("Mystery number has been set")
guess = input("enter a number as a guess to guess the number   ")
guessint = int(guess)
while guessint != compnum:
    if guessint > compnum:
        print("Your guess was too high")
    if guessint < compnum:
        print("Your guess was too low")
    guessint = input("enter a number as a guess to guess the number   ")
    guessint = int(guessint)
        


NUM = input("Please enter an number between 10 and 20   ")
NUMINT = int(NUM)
while NUMINT >= 20:
    print("Too High")
    NUM = input("Please try again  ")
    NUMINT = int(NUM)
    if NUMINT == NUMINT <= 20:
        print("Thank you")
        break
while NUMINT <= 10:
    print("Too Low")
    NUM = input("Please try again  ")
    NUMINT = int(NUM)
    if NUMINT == NUMINT >= 10:
        print("Thank you")
        break




num1 = 10
num2 = 9
print(num1, "green bottles sitting on the wall")
print("And if one green bottle should accidentally fall")
print("There'll be" ,num2, "green bottles sitting on the wall.")
print("And if one greeen bottle should accidentally fall")
num2 = num2 - 1
bottles = input("How many green bottles would be sitting on a wall?   ")
bottlesint = int(bottles)
while num2 > 0 :
    if bottlesint == num2:
        print("There are",bottles,"bottles sitting on a wall")
        print("And if one greeen bottle should accidentally fall")
        bottles = input("How many green bottles would be sitting on a wall?   ")
        bottlesint = int(bottles)
        num2 = num2 - 1
    else:
        bottles = input("No try again   ")
        bottlesint = int(bottles)
print("There are no more bottles sitting on a wall :c ")

    















    