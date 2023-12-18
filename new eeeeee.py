"""
num = input("Enter an Number  ")
numint = int(num)
print(num)
if numint % 2 ==  0:
    print("Your number is even")
if numint % 2 == 1:
    print("Your number is odd")

age = input("What is your age?  ")
ageint = int(age)
print(age)
if ageint >= 18:
    print("You can vote!")
if ageint < 18:
    print("You can not vote!")
    
inte1 = input("Input your first integer   ")
inte2 = input("Input your second integer   ")
print(inte1)
print(inte2)
inte1int = int(inte1)
inte2int = int(inte2)
greatest = []
if inte1int > inte2int:
    print(inte1,"is biiger than",inte2)
    greatest.append(inte1)
    print(greatest)
    output = inte1int
    print(output,"is the greatest number")
if inte2int > inte1int:
    print(inte2,"is bigger than",inte1)
    greatest.append(inte2)
    print(greatest)
    output = inte2int
    print(output,"is the greatest number")
if inte1int == inte2int:
    print("Both of your numbers have the same value")
    
usernum = input("Enter an number  ")
usernumint = int(usernum)
print(usernum)
if usernumint > 0:
    print("Posotive")
if usernumint < 0:
    print("Negative")
if usernumint == 0:
    print("Zero")
"""
age1 = input("Enter your age  ")
age1int = int(age1)
print(age1)
if age1int <= 12:
    catagory = "child"
    print(catagory)
if age1int > 12 < 19:
    catagory = "Teenager"
    print(catagory)
if age1int >= 59:
    catagory = "Adult"
    print(catagory)
