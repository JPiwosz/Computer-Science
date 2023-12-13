score = 0
chances = 6
word = "appliance"
game = "You Are Playing Hangman"
print(game)
figure = ["---------------- \n   o     |\n  /|\\    |\n  / \    |\n         |\n         |\n         |\n---------------\n","---------------- \n         |\n  /|\\    |\n  / \    |\n         |\n         |\n         |\n---------------\n"]
print(figure[0])
wordrange = len(word)

winningscore = int(len(word)) -2
print("The score you need to win is",winningscore)

wordlist = list(word)
print(wordlist)
guess = input("Take your first guess    ")
guesslower = guess.lower()


hiddenword = "_"
'''
hiddenwordlst = hiddenword * wordrange
hiddenwordlist = list(hiddenwordlst)
print(hiddenwordlist)'''

hiddenwordlist = '_ ' * 9
hiddenwordlist = hiddenwordlist.split()
print(hiddenwordlist)

for letter in range(wordrange):
    if word[letter] == guess:
        hiddenwordlist[letter] = guess
        print(hiddenwordlist)

if guess in word:
    score = score + 1

for space in range(wordrange):
    print(hiddenword, end = ' ')
    
while score != winningscore:
    print('score is: ',score)
    print('winningscore is: ',winningscore)
    guess = input("Guess Again Please ")
    guesslower = guess.lower()
    if guesslower in word:
        #score = score + 1
        #if score == winningscore:
            #print("Congrats you win, the word was",word)
        
        print("\nYour score is",score)
        print("\nGOOD GUESS!",guesslower,"WAS IN THE WORD!")
        print("Loading")
        indexofguess = wordlist.index(guess)
        print(indexofguess)
        guesscount = wordlist.count(guess)
        print(guesscount)
        print(wordlist[indexofguess])
        #for count in range(guesscount):
        del hiddenwordlist[indexofguess]
        #del wordlist[indexofguess]
        #print(wordlist)
        print(hiddenwordlist)
        hiddenwordlist.insert(indexofguess,guess)
        updatedlist = hiddenwordlist
        print(updatedlist)
        #guess = input("Guess Again Please ")
        #guesslower = guess.lower()
        
        score = score + 1
        if score == winningscore:
            print("Congrats you win, the word was",word)
        
        for letter in range(wordrange):
            if word[letter] == guess:
                hiddenwordlist[letter] = guess
                print(hiddenwordlist)
        '''
        score = score + 1    
        for letter in range(wordrange):
            if word[letter] == guess:
                hiddenwordlist[letter] = guess
                
        print(hiddenwordlist)
        guess = input("Guess Again Please   ")
        guesslower = guess.lower()
        '''

    if guess not in word:
        chances = chances -1
        print("You have",chances,"chances left")
        figure = ["---------------- \n   o     |\n  /|\\    |\n  / \    |\n         |\n         |\n         |\n---------------\n","---------------- \n         |\n  /|\\    |\n  / \    |\n         |\n         |\n         |\n---------------\n","---------------- \n         |\n  /|    |\n  / \    |\n         |\n         |\n         |\n---------------\n"]
        print(figure[2])

        
        if chances == 0:
            print("You loose :(")
            break
        
        #guess = input("Guess Again Please   ")
        #guesslower = guess.lower()

    
    if score == winningscore:
        print("Congrats you win, the word was",word)
    
    print('2nd score is: ',score)
    print('winningscore is: ',winningscore)
    

    
    
    
    
        
    
    
    
    
    
    
    
    
'''
for  i, element in enumerate(word) :
if element == guess:
hiddenwordlist[i] = guess
print(hiddenwordlist)
'''
        
        
