numberlist = ["123","456","789"]
for item in numberlist:
    print(item)
threedigetnumber = input("Please Write any three diget number  ")
if threedigetnumber in numberlist: 
    print(threedigetnumber)
else:
    print("That is not in the list")

partylist = input("Please name three people you want to invite to a party  ")
partylist1 = ([partylist])
print(type(partylist1))
print(partylist)

anyoneelse = input("Do you wish to invite anyone else perhaps  ")
anyoneelse1 = ([anyoneelse])
print(type(anyoneelse1))
print(anyoneelse1)
newlist = partylist1 + anyoneelse1
print(newlist)
