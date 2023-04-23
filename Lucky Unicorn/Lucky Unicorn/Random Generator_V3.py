# Calculate animal token percentages to ensure the house profits


import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 20 tokens

tokens = ["Unicorn", "Horse", "Horse", "Horse", "Donkey", "Donkey", "Donkey", "Zebra", "Zebra", "Zebra"]
for item in range(500):
    token = random.choice(tokens)

    # Calculate balance based on tokens generated

    if token == "Unicorn":
        balance += 4
    elif token == "Donkey":
        balance -= 1

    else:
        balance -= .5


    print(f"Token: {token} Balance: {balance: .2f}")
print(f"Starting Balance: {STARTING_BALANCE}")
print(f"Ending Balance: {balance}")
