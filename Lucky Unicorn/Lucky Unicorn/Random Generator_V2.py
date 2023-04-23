# Calculate animal token percentages to ensure the house profits


import random

balance = 100

# Testing loop to generate 20 tokens

tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]
for item in range(20):
    token = random.choice(tokens)
    print(token)
    # Calculate balance based on tokens generated

    if token == "Unicorn":
        balance += 4
    elif token == "Donkey":
        balance -= 1

    else:
        balance -= .5


    print(f"Token: {token} Balance: {balance: .2f}")
