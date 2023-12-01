score = 0
chances = 6
word = "appliance"
game = "You Are Playing Hangman"
print(game)
hangman = "--------------------\n                   |\n                   |\n                   |\n                   \n                   |\n               _____"
print(hangman)
wordrange = len(word)

wordlist = list(word)
print(wordlist)
guess = input("Take your first guess    ")
guesslower = guess.lower()

hiddenword = "_"
hiddenwordlst = hiddenword * wordrange
hiddenwordlist = list(hiddenwordlst)
print(hiddenwordlist)

for letter in range(wordrange):
    if word[letter] == guess:
        hiddenwordlist[letter] = guess
        print(hiddenwordlist)

for space in range(wordrange):
    print(hiddenword, end = ' ')
    
while guess != word:
    if guess in word:
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
        
        guess = input("Guess Again Please   ")
        guesslower = guess.lower()
        
        for letter in range(wordrange):
            if word[letter] == guess:
                hiddenwordlist[letter] = guess
                print(hiddenwordlist)
        '''
        for  i, element in enumerate(word) :
            if element == guess:
                hiddenwordlist[i] = guess
                print(hiddenwordlist)
        '''
        
        
