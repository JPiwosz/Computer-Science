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

