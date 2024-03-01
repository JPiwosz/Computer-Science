import logicgates

Menu = print("Choose one of the following gates , \n1 = NOT \n2 = AND \n3 = OR \n4 = XOR \n5 = NAND \n6 = NOR \n7 = XNOR")
MenuChoice = int(input("Input -->  "))

if MenuChoice == 1:
    print("You Have Chosen NOT Gate")
    print("Do you wish to see the truth table?")
    choice = input("y or n -->  ")
    if choice == "y":
        print("A  A(NOT)\n0  1\n1  0")
    input1 = int(input("Enter value for the Not Gate  "))
    print(logicgates.Not_Gate(input1))
    
if MenuChoice == 2:
    print("You Have Chosen AND Gate")
    print("Do you wish to see the truth table?")
    choice = input("y or n -->  ")
    if choice == "y":
        print("A  B  AB\n0  0  0\n1  0  0\n0  1  0\n1  1  1")
    input1 = int(input("Enter value for 'a'  "))
    input2 = int(input("Enter value for 'b'  "))
    print(logicgates.And_Gate(input1,input2))
    
if MenuChoice == 3:
    print("You Have Chosen OR Gate")
    print("Do you wish to see the truth table")
    choice = input("y or n -->  ")
    if choice == "y":
        print("A B AorB\n0  0  0\n1  0  1\n0  1  1\n1  1  0")
    input1 = int(input("Enter value for 'a'  "))
    input2 = int(input("Enter value for 'b'  "))
    print(logicgates.Or_Gate(input1,input2))
    
if MenuChoice == 4:
    print("You Have Chosen XOR Gate")
    print("Do you wish to see the truth table?")
    choice = input("y or n -->  ")
    if choice == "y":
        print("A B AXORB\n0  0  0\n0  1  1\n1  0  1\n1  1  1")
    input1 = int(input("Enter value for 'a'  "))
    input2 = int(input("Enter value for 'b'  "))
    print(logicgates.Xor_Gate(input1,input2))
    
