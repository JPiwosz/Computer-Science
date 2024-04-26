import random
Colourlist = []
P = 0
WinList = []
Random_Colour_List = ["red","yellow","green","pink","black","white","blue","purple"]
Start = input("Do you wish to start ?\n---> press y  ")
if Start == "y":
	print(Random_Colour_List)
	for i in range(4):
		Colourlist.append(random.choice(Random_Colour_List))
	print("Guess 4 colours with spaces in between them")
	Guess = input("---> ")
	Splitguess = Guess.split()
	print(Splitguess)
	if Splitguess == Colourlist:
		print("You win \nthe list was",Colourlist,"good job!")
		break
		for i in Splitguess:
			Ps = Splitlist.index(i)
			for v in Colourlist:
				Pc = Colourlist.index(v)
				RS = Splitlist.[Ps]
				RC = Colourlist.[Pc]
				if RS == RC:
					Winlist.append(RS)
					if WinList  = Colourlist:
						print("You win \nthe list was",Colourlist,"good job!")
						break