alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x","y", "z"]
#print(alphabet[1]) this prints a certain letter from the alphabet
message = input("Please enter your message    ")
key = input("Please enter the key   ")
key = int(key)
output = input("encoding or decoding , Press E for encoding or D for decoding    ")
output = output.lower()
if output == "e":
    print("Encoding Your Message Please Wait.....")
    empty = ""
    for i in message:
        Indexlist = alphabet.index(i)
        #print(Indexlist)
        idx = Indexlist + key
        if idx > 25:
            idx = idx %26
        #print(idx)
        idxn = alphabet[idx]
        #print(idxn)
        empty = empty + idxn
    print(empty)

if output == "d":
        print("Decoding Your Message Please Wait    ")
        empty = ""
        for i in message:
            Indexlist = alphabet.index(i)
        #print(Indexlist)
        idx = Indexlist + key
        if idx > 25:
            #print(idx)
            idxn = alphabet[idx]
            #print(idxn)
            empty = empty - idxn
        print(empty)
    