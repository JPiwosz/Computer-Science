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
    averadgeeven = 0
    averadgeodd = 0
    oddlist = []
    evenlist = []
    for i in a:
        if int(i)%2 == 0:
            even = even +1   #counts number of even numbers#
            evenlist.append(i)   #adds all even numbers to list#
            totaleven = totaleven + int(i)
            averadgeeven = int(totaleven) // int(len(evenlist))
        if int(i)%2 == 1:
            odd = odd +1
            oddlist.append(i)
            totalodd = totalodd + int(i)
            averadgeodd = int(totalodd) / int(len(oddlist))
    return even,odd,totalodd,totaleven,averadgeeven,averadgeodd