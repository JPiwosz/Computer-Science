"""
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
"""

compnum = 50
print("Mystery number has been set")
guess = input("enter a number as a guess to guess the number   ")
while guess == compnum:
    if guess > 50:
        print("Your guess was too high")
        if guess < 50:
            print("Your guess was too low")
    


















    