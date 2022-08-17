from classes import Word
from classes import Game

print("""

Let's Play Python Hangman Blankedy Blank Hybrid!

RULES         - Players have 6 attempts to guess a word or phrase.
              - Guesses are one character at a time
              - Incorrect guesses are shown below
WORD          - The word is set at the start (no peeking!)
              - The word cannot contain numbers.
              - Spaces are accepted and rendered accordingly
GAME END      - When either the player has guessed or ran out of attempts

Happy Guessing!!
""")

Game.gameLoop()
