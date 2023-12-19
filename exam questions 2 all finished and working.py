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

age1 = input("Enter your age  ")
age1int = int(age1)
print(age1)
if age1int <= 12:
    catagory = "child"
    print(catagory)
elif age1int > 12 and age1int <= 19:
    catagory = "Teenager"
    print(catagory)
elif age1int > 12 and age1int <= 59:
    catagory = "Adult"
    print(catagory)
elif age1int > 12 and age1int >= 60:
    catagory = "Senior Citizen"
    print(catagory)

"""
elif age1int > 12 and age1int > 19 and age1int <= 59:
    catagory = "Adult"
    print(catagory)
    
    THIS ALSO WORKS!!
"""


Daylist = ["Monday","Tuesday","Wensday","Thursday","Friday","Saterday","Sunday"]
numb = input("Enter an number from 1 - 7  ")
numbint = int(numb)
if numbint < 1 or numbint > 7:
    print("User Error")
elif numbint >= 1 or numbint <= 7:
    rangenumb = numbint - 1
    Day = Daylist[rangenumb]
    print(Day)
    
userweight = input("Enter your weight in kilograms  ")
userheight = input("Enter your height in meters  ")
userweightint = int(userweight)
userheightint = int(userheight)
BMI = 0
BMI = userweightint / (userheightint * userheightint)
BMIint = int(BMI)
print(BMIint)
if BMIint < 18.5:
    Class = "UnderWeight"
    print(Class)
elif BMIint >= 18.5 and BMIint <= 24.9:
    Class = "Normal Weight"
    print(Class)
elif BMIint >= 25 and BMIint <= 29.9:
    Class = "Overweight"
    print(Class)
elif BMIint >= 30:
    Class = "Obesity"
    print(Class)

subject1 = input("Enter Grade in percentadge   ")
subject2 = input("Enter Grade in percentadge   ")
subject3 = input("Enter Grade in percentadge   ")
subj1f = float(subject1)
subj2f = float(subject2)
subj3f = float(subject3)
averagegrade = (subj1f + subj2f + subj3f) / 3
roundedgrade = round(averagegrade,2)
print("Your average grade is",roundedgrade)
if roundedgrade >= 90 and roundedgrade <= 100:
    Grade = "A"
    print(Grade)
elif roundedgrade >= 80 and roundedgrade <= 89:
    Grade = "B"
    print(Grade)
elif roundedgrade >= 70 and roundedgrade <= 79:
    Grade = "C"
    print(Grade)
elif roundedgrade >= 60 and roundedgrade <= 69:
    Grade = "D"
    print(Grade)
elif roundedgrade >= 0 and roundedgrade <= 59:
    Grade = "F"
    print(Grade)
print("Your Average grade was",Grade)
