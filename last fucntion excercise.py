


namelist = []

def choice1(namelist):
    addname = input("Enter The Name You Want To Add To The List   ")
    namelist.append(addname)
    print(namelist)
    return(namelist)
    
def choice2(namelist):
    print(namelist)
    deletename = input("Enter The Name You Want To Delete From The List   ")
    print(namelist)
    indexpos = namelist.index(deletename)
    print(indexpos)
    del namelist[indexpos]
    return(namelist)

def choice3(namelist):
    changename = input("Enter the name you wish to change   ")
    indexpos1 = namelist.index(changename)
    print(indexpos1)
    del namelist[indexpos1]
    
    changedname = input("Enter what you want to change that name to   ")
    namelist.insert(indexpos1,changedname)
    return(namelist)

def choice4(namelist):
    displaylist = namelist
    print(displaylist)
    return(namelist)

def menu():
        menu1 = "1) Add a Name \n2) Delete a Name \n3) Change a Name \n4) View All Names In The List \n5) End The Program"
        print(menu1)
        menuchoice = input("Select ->   ")
        print(menuchoice)
    
        if not menuchoice.isdigit():
            print("Selected Number was not between 1 and 5")
    
        elif int(menuchoice) < 1 or int(menuchoice) > 5:
            print("Selcted Number was not between 1 and 5")
        else:
            menuchoiceint = int(menuchoice)
        return menuchoiceint


menuchoice = menu()  
while menuchoice != 5:
    if int(menuchoice) == 1:
        A = choice1(namelist)
    if int(menuchoice) == 2:
        B = choice2(namelist)
    if int(menuchoice) == 3:
        C = choice3(namelist)
    if int(menuchoice) == 4:
        D = choice4(namelist)
    menuchoice = menu()  

    

    
        
    
    
    


    
    



































