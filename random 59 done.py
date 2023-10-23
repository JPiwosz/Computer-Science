import random
colours = random.choice(["red","green","blue","yellow","black"])
print(colours)
usercolour = input("Please pick an colour    ")
if usercolour == colours:
    print("Well Done!")
elif usercolour != colours:
    print("Your poo is",colours)
guessagain = input("Guess Again   ")
coloursup = colours.upper()
while guessagain != colours:
    print("YOUR POO IS",coloursup)
    guessagain = input("Guess once again  ")
    if guessagain == colours:
        print("Well Done")
