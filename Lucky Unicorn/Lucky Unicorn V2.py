

player_money = int(input("How much money do you have?"))
money_gained = 0
money_lost = 0
round_money = player_money - money_lost + money_gained

play_round = input("Do you want to play a round?")
import random
tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]


# Testing Loop to make 20 Tokens


for item in range(20):
    token = random.choice(tokens)
    print(token, end = '\t')
