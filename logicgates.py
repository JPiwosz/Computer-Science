
def Not_Gate (a):
    if a == 1:
        return 0
    else:
        return 1
        
def And_Gate (a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def Or_Gate (a,b):
    if a or b == 1:
        return 1
    else:
        return 0
    
def Xor_Gate (a,b):
    if a == 1 and b == 1:
        return 0
    if a == 1 and b == 0:
        return 1
    if a == 0 and b == 1:
        return 1
    else:
        return 0
        


