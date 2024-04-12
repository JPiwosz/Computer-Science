"""
print("Press ''y'' to start")
start = input("----> ")
if start == "y":
    inptemp = input("Enter Tempature in degrees C \n----> ")
    f = 9.0/5.0
    F = f
    fer = (int(inptemp) * F) + 32
    print("That is",fer,"in degrees fahrenheit")
"""
   
print("Press ''y'' to start")
start = input("----> ")
if start == "y":
    inptemp = input("Enter Tempature in degrees F \n----> ")
    C = (int(inptemp)-32) *5/9
    print(C)
    