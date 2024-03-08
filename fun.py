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
    odd = int(1)
    even = int(0)
    oddlist = []
    evenlist = []
    for i in a:
        if i%2 == 0:
            even = even +1
            evenlist.append(i)
        if i%2 == 1:
            odd = odd +1
            oddlist.append(i)
    return even,odd
    
                
    