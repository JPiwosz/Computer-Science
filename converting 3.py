menu = "1: Binary Numbers to Decimal Numbers.\n2: Decimal Numbers to Binary Numbers.\n3: Add Two Binary Numbers.\n4: Decimal Number into Hexadecimal"
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
    newnum = []
    R = 0
    carry = 0
    startnum = 0
    startnum2 = 0
    print(binnum1,binnum2)
    lenbinnum1 = len(binnum1)
    lenbinnum2 = len(binnum2)
    for i in range(lenbinnum1):
        startnum = startnum - 1
        variable1 = binnum1[startnum]
        variable2 = binnum2[startnum]
        newvari = int(variable1) + int(variable2) + carry
        if newvari > 1:
            carry = 1
            if newvari == 2:
                newnum.append(0)
            else: newnum.append(1)
        else:
            carry = 0
            newnum.append(newvari)
            carry = carry - carry
    if carry == 1:
        newnum.append(carry)
        newnum.reverse()
        print("Final list is",newnum)
        

if choiceint == 4:
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15
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
        
        
        
        
        
        
        
        

