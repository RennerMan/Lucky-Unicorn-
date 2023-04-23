# Calculate Balance from a list of random animal tokens


import random

tokens = ["Unicorn", "Horse", "Zebra", "Donkey", "Horse", "Zebra", "Donkey", "Horse", "Zebra", "Donkey"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE
# Testing loop to generate 20 tokens


for item in range(100):
    token = random.choice(tokens)
    print(token, end='\t')

    # Calculate balance based on tokens generated

    if token == "Unicorn":
        balance += 4
    elif token == "Horse":
        balance -= .5
    elif token == "Zebra":
        balance -= .5
    else:
        balance -= 1
print(f"Starting Balance = ${STARTING_BALANCE:.2f}")
print(f"Final Balance = ${balance:.2f}")
# Tells you how much money made/lost to make testing easier


if balance > 100:
    print(f"you made ${balance - 100}!")
elif balance < 100:
    print(f"you lost ${balance - 100} :(")
