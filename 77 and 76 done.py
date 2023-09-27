partylist1 = []

partylist = input("Please name three people you want to invite to a party  ")
partylist1.append(partylist) #= list(partylist)
print(type(partylist1))
print(partylist1)

anyoneelse = input("Do you wish to invite anyone else perhaps  ")
while True:
    
    anyoneelse1 = list(anyoneelse)
    print(type(anyoneelse1))
    print(anyoneelse1)
    partylist1 = partylist1 + anyoneelse1
    print(partylist1)
    anyoneelse = input("Do you wish to invite anyone else perhaps  ")
    anyoneelse = anyoneelse.upper()
    if anyoneelse == "NO":
        print("Your list of people who are coming to the party are", partylist1)
        break
   
