opening = open ("C:\\Users\\20JPiwosz.ACC\\Downloads\\numbers.txt",'r')
for line  in opening:
    print(line.strip())
opening.close()