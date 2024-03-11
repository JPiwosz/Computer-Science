def Add_Two (a,b):
    total = a + b
    return total

def Un_Adder (a):
    wordnew = "un" + a
    return wordnew

def Palin (a):
    F = list(a)
    
    G = list(a)
    F.reverse()
    if G == F:
        return "True"
    else:
        return "False"

def Odd_And_Even (a,b):
    for i in b:
        a.append(i)
    print(a)
    odd = 0
    even = 0
    totalodd = 0
    totaleven = 0
    oddlist = []
    evenlist = []
    for i in a:
        if int(i)%2 == 0:
            even = even +1
            evenlist.append(i)
        if int(i)%2 == 1:
            odd = odd +1
            oddlist.append(i)
            for i in oddlist:
                num = oddlist[-i]
                totalodd = 0 + int(num)
    return even,odd,totalodd

    
                
    