list1 = [1,1,0,1,1]
byte1 = [0,0,0,0,0,0,0,0]
pos = 0
lenlist = len(list1)
for i in list1:
    pos = pos - 1
    print("Posistion is",pos)
    byte1[pos]=i
    print(byte1)