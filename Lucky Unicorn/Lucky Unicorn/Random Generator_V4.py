# Calculate animal token percentages to ensure the house profits: use percentages to ensure house profit


import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE
# Testing loop to generate 500 tokens
token = 0

for item in range(500):
    number = random.randint(1, 100)
    print(number)
    # Calculate balance based on tokens generated

    if 1 <= number <= 5:
        token = "Unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "Donkey"
        balance -= 1
    elif number % 2 == 0:
        token = "Horse"
        balance -= .5

    else:
        token = "Zebra"
        balance -= .5

print(f"Token: {token} Balance: {balance: .2f}")
print(f"Starting Balance = ${STARTING_BALANCE:.2f}")
print(f"Final Balance = ${balance:.2f}")
# Tells you how much money made/lost to make testing easier


if balance > 100:
    print(f"you made ${balance - STARTING_BALANCE}!")
elif balance < 100:
    print(f"you lost ${balance - STARTING_BALANCE} :(")
