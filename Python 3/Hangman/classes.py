from stickman import *
import os

word = ""
guess = ""
lower_word = word.lower()
guessed = []
hidden_word = []
already = False

class Word:

    def __init__(self):
        self.word = word = ""
        self.lowerword = word.lower()
        self.guessed = guessed = []
        self.hidden = hidden_word = []

    def setWord(self):
        global word
        word = input("Set the word to be guessed. : ")
        for i in range(0, len(word), 1):
            for letter in word:
                try:
                    int(letter)
                    print("Numbers are not allowed!")
                    return self.setWord()
                except ValueError:
                    self.word = word.lower()

    def printHidden():
        for i in hidden_word:
            print(i.upper(), end = " ")
        print ("")
        print ("")

    def printGuessed():
        global already
        print("Incorrect letters: ", end = " ")
        if not guessed:
            pass
        else:
            for i in guessed:
                print(i.upper(), end = " ")
        if len(guess) > 1:
            print("Please guess one letter at a time.")
        else:
            print ("")
        if already:
            print("Already guessed!")
            already = False



    def testWon():
        test = ""
        space_test = ""
        for i in hidden_word:
            test += i.lower()
            if "   " in test:
                space_test = test.replace("   ", " ")
            if test == word.lower() or space_test == word.lower():
                print("""
Great Merlin's Beard!!!!
You managed to guess the word.
Which if it wasn't obvious by now was...

{word}

Have yourself a cookie or something to celebrate.""".format(word=word))
                exit()

class Game:
    def __init__(self, word):
        self.attempts = 0

    def gameLoop():
        hangman = Word()
        hangman.setWord()
        game = Game(hangman.word)
        game.hideWord()
        while game.attempts != 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            Word.testWon()
            game.compareHidden(game.setGuess())
        print(position_7)
        print("""
You did not win this time!
But you can always play again...
Unless you're late for something, I dunno...
You do you.
Bye!!!!!""")

    def setGuess(self):
        global guess
        global guessed
        global already
        if already:
            os.system('cls' if os.name == 'nt' else 'clear')
        self.drawHangman()
        Word.printHidden()
        Word.printGuessed()
        guess = input("Guess a letter: ")
        if len(guess) > 1:
            self.setGuess()
        for i in guessed:
            if i == guess:
                if len(guessed) == 0:
                    pass
                else:
                    already = True
                    return self.setGuess()
        try:
            int(guess)
            print("Numbers are not allowed!")
            return self.setGuess()
        except ValueError:
            return guess.lower()

    def hideWord(self):
        global hidden_word
        if word.count(" ") == 0:
            for i in range(0,len(word), 1):
                hidden_word.append(" _ ")
        else:
            for i in range(0,len(word), 1):
                if word[i] != " ":
                    hidden_word.append(" _ ")
                else:
                    hidden_word.append("   ")
        print("")

    def compareHidden(self, guess):
        match_index = []
        for i in range(0,len(word),1):
            if word[i].lower() == guess.lower():
                match_index.append(i)
        for i in match_index:
            hidden_word[i] = guess
        Word.printHidden()
        if guess.lower() not in word.lower():
            self.attempts += 1
            guessed.append(guess)

    def drawHangman(self):
        if self.attempts == 0:
            print(position_1)
        if self.attempts == 1:
            print(position_2)
        if self.attempts == 2:
            print(position_3)
        if self.attempts == 3:
            print(position_4)
        if self.attempts == 4:
            print(position_5)
        if self.attempts == 5:
            print(position_6)
