import os
from random import choice
from questions import *

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 0
        self.banked = 0

    def __repr__(self):
        return "The player is called " + self.name + "."

class Game:

    def __init__(self):
        self.question = 1
        self.difficulty = 0
        self.money = 0
        self.q_list = []
        self.asked_keys = []
        self.gone_bust = False
        self.a_diff = 0

    def setGame():
        global game
        global player
        print("\x1b[8;50;100t")
        name = input("Enter your name: ")
        player = Player(name)
        game = Game()
        game.response(0)
        while player.lives > -1:
            game.askQuestion()
            game.checkAnswer(game.setAnswer())
            game.setDifficult()
        game.endGame()

    def askQuestion(self):
        if game.difficulty == 0:
            print('Question Number {question}'.format(diff=game.difficulty,question=game.question))
        else:
            print(f'Difficulty Level {game.difficulty}. Question Number {game.question}')
        if game.difficulty == 0:
            rand_num = choice([i for i in range(1,len(a_questions)+1) if i not in game.asked_keys])
            game.q_list = a_questions.get(rand_num)
            game.asked_keys.append(rand_num)
        if game.difficulty == 1:
            rand_num = choice([i for i in range(1,len(b_questions)+1) if i not in game.asked_keys])
            game.q_list = b_questions.get(rand_num)
            game.asked_keys.append(rand_num)
        if game.difficulty == 2:
            rand_num = choice([i for i in range(1,len(c_questions)+1) if i not in game.asked_keys])
            game.q_list = c_questions.get(rand_num)
            game.asked_keys.append(rand_num)
        if game.difficulty == 3:
            rand_num = choice([i for i in range(1,len(d_questions)+1) if i not in game.asked_keys])
            game.q_list = d_questions.get(rand_num)
            game.asked_keys.append(rand_num)
        return print(game.q_list[0])


    def setAnswer(self):
        setattr(game, "user_answer", "")
        game.user_answer = input('What do you recon? : ')
        if game.user_answer.lower() == 'bank':
            game.endGame()
        try:
            int(game.user_answer)
            return game.user_answer
        except ValueError:
            game.response(3)
            print(game.q_list[0])
            return game.setAnswer()

    def checkAnswer(self, user_answer):
        game.a_diff = game.q_list[1] - int(user_answer)
        game.question += 1
        if game.difficulty == 0:
            if game.a_diff == 0:
                player.lives += 5
                return game.response(1)
            return game.response(4)
        else:
            game.addMoney()
            if int(user_answer) > game.q_list[1]:
                game.gone_bust = True
                game.endGame()
            if game.a_diff == 0:
                player.lives += (5 * game.difficulty)
                game.bankMoney()
                return game.response(1)
            player.lives -= game.a_diff
            return game.response(2)

    def addMoney(self):
        setattr(game, "gained", 0)
        if game.difficulty == 1:
            game.gained = 1000 * int(game.user_answer)
            game.money += game.gained
        elif game.difficulty == 2:
            game.gained = 2000 * int(game.user_answer)
            game.money += game.gained
        elif game.difficulty == 3:
            game.gained = 2500 * int(game.user_answer)
            game.money += game.gained
        elif game.difficulty == 4:
            game.gained = 4000 * int(game.user_answer)
            game.money += game.gained

    def bankMoney(self):
        player.banked = game.money

    def setDifficult(self):
        if game.question == 6 and game.difficulty == 0:
            game.difficulty += 1
            game.question = 1
            game.response(6)
            game.asked_keys.clear()
        if game.question >= 11:
            game.difficulty += 1
            game.question = 1
            game.asked_keys.clear()
            game.response(6)
        return self.difficulty

    def endGame(self):
            if player.lives >= -1 and game.user_answer.lower() != "bank":
                self.response(5)
                return exit()
            else:
                self.response(7)
                return exit()
            return exit()

    def response(self, num):
        if num == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            return print(f"""
====================================================================================================
                                  **** LIVE BUILDING PHASE ****
====================================================================================================

                             Welcome {player.name}!! Let's play...
            """)
        if num == 1 and game.difficulty == 0:
            return print("""
**** CORRECT! ****

You now have: {lives} lives.
""".format(money=game.money,banked=player.banked,lives=player.lives))
        elif num == 1:
            return print(f"""
**** CORRECT! ****

You gained £{game.gained} and have banked £{player.banked}.
You have {player.lives} lives remaining.
""")
        elif num == 2:
            return print(f"""
**** INCORRECT! ****

The Correct Answer was {game.q_list[1]}.
You played {game.user_answer} so the money total now stands at £{game.money}
You have {player.lives} lives remaining.
You have £{player.banked} banked to take with BANK.
""")
        elif num == 3:
            return print(f"""
**** Invalid Option ****

Please enter a whole Number to play.
Enter LIVES for lives remaining.
Or BANK to end with your banked amount of {player.banked}!
""")
        elif num == 4:
            print(f"""
**** INCORRECT! ****

The Correct Answer was {game.q_list[1]}.
You played {game.user_answer} so were {abs(game.a_diff)} away.

**** Since this is the first phase no lives were lost. ****
""")
        elif num == 5 and game.gone_bust:
            print(f"""
**** GUESS TOO HIGH!! ****

You leave with £0!! :(
The Correct Answer was {game.q_list[1]}.
You played {game.user_answer} so were {abs(game.a_diff)} away""")
        elif num == 5:
            print(f"""
**** OUT OF LIVES!!! :( ****

The Correct Answer was {game.q_list[1]}.
You played {game.user_answer} so were {abs(game.a_diff)} away""")
        elif num == 6 and game.difficulty > 0:
            input("Press enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
====================================================================================================
                                     **** MAIN GAME PHASE ****
====================================================================================================

Difficulty has been increased to Level {game.difficulty}.
You currently have {player.lives} lives remaining and have banked £{player.banked}.
""")
        elif num == 6:
            input("Press enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
====================================================================================================
                                     **** MAIN GAME PHASE ****
====================================================================================================

You managed to accumilate: {player.lives} lives.
Use them wisely.
""")
        elif num == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
====================================================================================================
                                     **** WINNER!!! ****
====================================================================================================
                                    Congratulations {player.name}

   I8,        8        ,8I    88    888b      88    888b      88    88888888888    88888888ba
   `8b       d8b       d8'    88    8888b     88    8888b     88    88             88      "8b
    "8,     ,8"8,     ,8"     88    88 `8b    88    88 `8b    88    88             88      ,8P
     Y8     8P Y8     8P      88    88  `8b   88    88  `8b   88    88aaaaa        88aaaaaa8P'
     `8b   d8' `8b   d8'      88    88   `8b  88    88   `8b  88    88             88    88'
      `8a a8'   `8a a8'       88    88    `8b 88    88    `8b 88    88             88    `8b
       `8a8'     `8a8'        88    88     `8888    88     `8888    88             88     `8b
        `8'       `8'         88    88      `888    88      `888    88888888888    88      `8b

                                 You have left with £{player.banked}.

""")
