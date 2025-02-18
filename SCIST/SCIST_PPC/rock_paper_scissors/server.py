import random
from flag import flag

def ascii_art(bot):
    print("bot > ")
    if bot == 0:
        # Rock 0
        print("""
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
        """)

    elif bot == 1:
        # Paper 1
        print("""
     _______
---'    ____)____
            ______)
            _______)
            _______)
---.__________)
        """)

    elif bot == 2:
        # Scissors 2
        print("""
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
        """)


def winOrlose(bot,player):
    if bot == 0 and player == 2:
       return("Bot WIN!")

    elif bot == 1 and player == 0:
       return("Bot WIN!")

    elif bot == 2 and player == 1:
       return("Bot WIN!")

    elif bot == player:
        return("It's a tie!")

    else:
        return("Player wins")

def main():
    print('''
=====================
 ROCK PAPER SCISSORS
=====================   
Rules:
You must play rock-paper-scissors with the robot 100 times!
Note: This robot is a bit silly and always makes the first move.
    ''')
    for i in range(100):
        bot = random.randint(0, 2)
        print('''        
=====================
        ''')
        ascii_art(bot)
        print('''
=====================
rock = 0
paper = 1
scissors = 2
---------------------
        ''')
        player = int(input('player > '))

        print(winOrlose(bot,player))

    print(flag)

main()

