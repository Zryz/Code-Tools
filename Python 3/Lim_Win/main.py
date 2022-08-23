from l_win import Player
from l_win import Game
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("""

====================================================================================================
                                **** WELCOME TO LIMITLESS WIN ****
====================================================================================================

FORMAT      - The answer to all questions are given as whole numbers only.
            - Decimals are not accepted.

PHASES      - The game has two phases. A lives accuilation phase, and a main game phase.
            - During lives accumilation any number is accepted but only exact answers earn lives.
            - During the main game phase the following rules apply.

RULES       - Answers higher than the correct answer forfeit the game.
            - Correct answers bank the money total and earns player lives.
            - Lives protect players when they answer below the correct answer.
            - The amount below the correct answer is deducted from their Lives total.
            - The greater the difficuly, the quicker the money total increases.
            - The money total increases relative to a players answer.

END         - After each question your total lives and banked money are displayed.
            - When you feel you cannot risk losing type BANK to leave and win the game.
            - BANK is case-insensitive i.e bAnk and BANK are both acceptable.
"""
)

Game.setGame()
