import math 
"""
print("Hello what is your name?  ")
username = input("What is your name?   ")
print("Weclome",username,"!")

integer1 = input("Enter your first Integer  ")
integer2 = input("Enter your second Integer  ")
sumofint = int(integer1) + int(integer2)
print(sumofint)

user_tempature = input("Enter an Tempature in degrees celcius  ")
celtemp = int(user_tempature)
fertemp = 9/5 * celtemp + 32
print(fertemp)

principle = input("Enter Princible ")
rate = input("ENTER Rate ")
time = input("Enter Time ")
principleint = int(principle)
rateint = int(rate)
timeint = int(time)
simple_interest = principleint * rateint * timeint / 100
print("Simple Interest is",simple_interest)

seconds = input("Enter an amount of seconds  ")
secsint = int(seconds)
print(secsint)
hours1 = secsint / 60 / 60
hoursint = int(hours1)
leftoverhours = hours1 - hoursint
minutes1 = leftoverhours * 60
minutesint = int(minutes1)
leftoverminutes = minutes1 - minutesint
seconds1 = leftoverminutes * 60
secondsint = int(seconds1)
print("Hours:",hoursint,"\nMinutes:",minutesint,"\nSeconds:",secondsint)

Monkeys = 0
Bananas = 0
Monkeysint = int(Monkeys)
Bananasint = int(Bananas)
add1 = input("Enter a number to add to variable1   ")
add2 = input("Enter a number to add to variable2   ")
add1int = int(add1)
add2int = int(add2)
Monkeysint = Monkeysint + add1int
print("There is",Monkeysint,"Monkeys!")
Bananasint = Bananasint + add2int
print("There is",Bananasint,"Bananas!")
print("\n!!Reverse!!\n")

Monke = Bananasint
print(Monke)
Banan = Monkeysint
print(Banan)

Monkeysint, Bananasint = Bananasint,Monkeysint
print("Now there is",Monkeysint,"Monkeys!")
print("Now there is",Bananasint,"Bananas!")



radius = input("Enter the radius of the circle  ")
radiusint = int(radius)
area = 0
area = math.pi * radiusint**2
areaR = round(area,0)
areaint = int(areaR)
print("The area of the circle is",areaint,"!")
circumfrance = 0
circumfrance = 2 * math.pi * radiusint
circumfranceR = round(circumfrance,0)
circumfranceint = int(circumfranceR)
print("The circumfrance of the circle is",circumfranceint,"!")

length = input("Enter length of rectangle  ")
width = input("Enter width of rectangle  ")
widthint = int(width)
lengthint = int(length)
Area = 0
Area = widthint * lengthint
print("The area of the rectangle is",Area,"!")
Circumfrance = 0
Circumfrance = 2 * (lengthint + widthint)
print("The Circumfrance of the circle is",Circumfrance,"!")

ap = input("Enter Number  ")
bp = input("Enter Number  ")
cp = input("Enter Number  ")
a = int(ap)
b = int(ap)
c = int(cp)
s = 0
s = (a + b + c) / 2
S = s*(s-a)*(s-b)*(s-c)
AreaT = math.sqrt(S)
AreaTR = round(AreaT,2)
print("The Area of the triangle is",AreaTR)
"""

CompoundInterest = 0
principle1 = input("Enter Princible ")
rate1 = input("ENTER Rate ")
time1 = input("Enter Time ")
timeINT = int(time1)
rateINT = int(rate1)
prinINT = int(principle1)
CI = prinINT*(1+rateINT/100)**timeINT - prinINT
print(CI)









