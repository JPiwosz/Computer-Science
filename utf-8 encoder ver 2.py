print("Please enter your sentence")
sentence = input("----> ")
pos = 0
BinaryStrip = ""
Byte1 = [0,0,0,0,0,0,0,0]
typebyte = type(Byte1)
print(typebyte)
print(Byte1)
senlist = list(sentence)
print(sentence)
"""
senlist.remove[0]
senlist.remove[-1]
"""
print(senlist)
for i  in senlist:
    Byte1 = [0,0,0,0,0,0,0,0]
    pos = 0
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
    print("in binary is",binarylist)
    binarylistlen = len(binarylist)
    print(binarylistlen)
    binarylist.reverse()
    if binarylistlen <= 7:
        print("Byte 1")
        for i in binarylist:
            pos = pos - 1
            print("posistion is",pos)
            Byte1[pos] = i
            print(Byte1)
            BinaryStrip = Byte1
            print("Binary Strip is",BinaryStrip)
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
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

    
    
