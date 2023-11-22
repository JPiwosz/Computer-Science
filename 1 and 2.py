opening = open ("C:\\Users\\20JPiwosz.ACC\\Downloads\\numbers.txt",'r')

total = 0
for line in opening:
    x = line.strip()
    if x != "":
        x = int(x)
        total = total + x
    print(total)
        
opening.close()