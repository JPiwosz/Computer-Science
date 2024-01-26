menu = "1: Binary Numbers to Decimal Numbers.\n2: Decimal Numbers to Binary Numbers.\n3: Add Two Binary Numbers."
print(menu)
choice = input("Please choose one of the given options   ")
choiceint = int(choice)
print(choiceint)


if choiceint == 1:
    urnumbinary1 = input("Enter your binary number  ")
    x = len(urnumbinary1) -1
    total = 0
    for i in urnumbinary1 :
        if i == "1":
            total = total + (2**x)
        else : total = total + 0
        x = x-1
    print("In Binary your Decimal number is",total)
        
if choiceint == 2:
    decimalnum1 = input("Enter your decimal number  ")
    y = len(decimalnum1)
    binarylist = []
    decimalnum1int = int(decimalnum1)
    while decimalnum1int != 0:
        decimalnum1left = decimalnum1int % 2
        decimalnum1int = decimalnum1int // 2
        binarylist.append(decimalnum1left)
    binarylist.reverse()
    print("Your Decimal number in Binary is",binarylist)

"""
if choiceint == 3:
    print("You will be asked to enter the two binary numbers you wish to add togther")
    binnum1 = input("Enter your first binary number  ")
    binnum2 = input("Enter your second binary number  ")
    print(binnum1,binnum2)
    x = len(binnum1) -1
    total1 = 0
    for i in binnum1 :
        if i == "1":
            total1 = total1 + (2**x)
        else : total1 = total1 + 0
        x = x-1
    print("Your first Binary your Decimal number is",total1)
    x = len(binnum2) -1
    total2 = 0
    for i in binnum2 :
        if i == "1":
            total2 = total2 + (2**x)
        else : total2 = total2 + 0
        x = x-1
    print("Your Second Binary your Decimal number is",total2)
    totaloftotals = int(total1) + int(total2)
    print("Your two binary numbers added togther in decimal are",totaloftotals)
    totaloftotals = str(totaloftotals)
    y = len(totaloftotals)
    binarylist = []
    totaloftotalsint = int(totaloftotals)
    while totaloftotalsint != 0:
        totaloftotalsleft = totaloftotalsint % 2
        totaloftotalsint = totaloftotalsint // 2
        binarylist.append(totaloftotalsleft)
    binarylist.reverse()  
    print("Your Decimal number in Binary is",binarylist)
"""

if choiceint == 3:
    print("You will be asked to enter the two binary numbers you wish to add togther")
    binnum1 = input("Enter your first binary number  ")
    binnum2 = input("Enter your second binary number  ")
    print(binnum1,binnum2)
    print(binnum1[-1])
    for i in range(len(binnum1)):
        lenofbin1 = len(binnum1)
        suma = int(i) - int(lenofbin1)
        print(suma)
        last = binnum1[-1]
        print(last)
        print(binnum1[int(last)])
        
    #for b in range(len(binnum2)):
        #print("Working")
        #lastb = binnum2[-1]
        #print(lastb)
        
    
        
    



