name = input("Please enter your name once again  ")
print(name)
nameupd = len(name)
print(nameupd)
for d in range(nameupd):
    print(name[d])
num2 = input("Please enter a number  ")
num2new = int(num2)
for f in range(num2new):
    for d in range(nameupd):
        print(name[d])


tablenumber = input("Please give me an number between 1 and 12   ")
tablenumber1 = int(tablenumber)
print(tablenumber1)
if tablenumber1 > 12:
    print("ERROR!!!")
else:
    print("The Times Table for", tablenumber, "is")
    table = 13
    for i in range(table):
        print(tablenumber1,"by",i,"=",tablenumber1*i)

lt50 = input("Please Write an Number that is less than  50  ") #lt50 = lessthen50
lt50n = int(lt50)
print(lt50)
if lt50n >= 50:
    print("ERROR!!!")
else:
    while lt50n < 50:
        print(lt50n + 1)
        lt50n = lt50n + 1
    
name = input("Please enter your name once again  ")
print(name)
num2 = input("Please enter a number  ")
num2new = int(num2)
if num2new > 10:
    for num2new in range(3):
        print("Too high")
else:
    for num2new in range(num2new):
        print(name)
         


        