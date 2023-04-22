# Component 1: ask user if they have played before


show_instructions = ""
while show_instructions != "x":
    show_instructions = input("have you played the game before?").lower().
    if show_instructions == "yes" or show_instructions == "y":
    print("program continues")
elif show_instructions == "no" or show_instructions == "n":
    print("display instructions")
else:
    print("please pick either yes or no")



player_money = int(input("How much money do you have?"))
money_made = 0
round_money = player_money +- money_made

play_round = input("Do you want to play a round?")
import random
tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]


# Testing Loop to make 20 Tokens


for item in range(20):
    token = random.choice(tokens)
    print(token, end = '\t')
