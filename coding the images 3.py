
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
	print(Colourlist)
	Guess = input("---> ")
	Splitguess = Guess.split()
	print(Splitguess)
	if Splitguess == Colourlist:
		print("You win \nthe list was",Colourlist,"good job!")
	else:
		for i in Splitguess:
			for v in Colourlist:
				Ps = Splitguess.index(i)
				Pc = Colourlist.index(v)
				RS = Splitguess[Ps]
				RC = Colourlist[Pc]
				if RS == RC:
					print(RS,"Is in the list")
					if Ps == Pc:
						print(RS,"In the list at correct posistion")
						WinList.append(RS)
					else:
						print(RS,"In the list at wrong position")
				if WinList  == Colourlist:
					print("You win \nthe list was",Colourlist,"good job!")
				else:
					print("The colours did not match their corresponding posistions")
					guessagain = input("Guess Again Please\n---> ")
					guessagainsplit = guessagain.split()
					print(guessagainsplit)