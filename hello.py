from datetime import datetime
from random import randint

world = 'World 🌍🌎🌏'
python = 'Python 🐍'
fire = '🎲'

def roll_a_dice():
    roll = randint(1,6)
    print(f"You rolled a {roll} {fire * roll}")

print(f"Hello {world} !\n")
print(f"Welcome to {python} !\n")
print(f"{python} is good for Maths!")
print(f"3 vezes nove é {3*9}!\n")
print(f"The date and time is {datetime.now()}\n")
roll_a_dice()
roll_a_dice()
roll_a_dice()