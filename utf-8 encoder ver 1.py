print("Please enter your sentence")
sentence = input("---->   ")
senlist = list(sentence)
print(sentence)
"""
senlist.remove[0]
senlist.remove[-1]
"""
print(senlist)
for i  in senlist:
    uni = ord(i)
    print(uni)
    """
    letter = chr(uni)
    print(letter)
    """
    decimalnum1 = str(uni)
    y = len(decimalnum1)
    binarylist = []
    decimalnum1int = int(decimalnum1)
    while decimalnum1int != 0:
        decimalnum1left = decimalnum1int % 2
        decimalnum1int = decimalnum1int // 2
        binarylist.append(decimalnum1left)
    binarylist.reverse()
    print("in binary is",binarylist)
    binarylistlen = len(binarylist)
    print(binarylistlen)
    if binarylistlen >= 7:
        print("Byte 1")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    if binarylist[0] == 0:
        binarylist.remove[0]
        print(binarylist)
    if binarylist[0:3] == 110:
        binarylist.remove[0:3]
        print(binarylist)
    """
    """
    for i in binarylist:
        print(i)
    """

    
    
