# Component 4: game mechanics and looping. Removed Hard-Wiring. Gives user feedback

import random

TEST_AMOUNT = 5
balance = TEST_AMOUNT
rounds_played = 0
play_again = ""

# testing loop to make 5 tokens
while play_again != "x".upper():
    rounds_played += 1
    number = random.randint(1, 100)

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
    if balance < 1:
        print("You ran out of money!")
        play_again = "x"
    else:
        play_again = input("Do you want to play again?\n Input anything but x to play again")

print(f"Starting Balance = ${TEST_AMOUNT:.2f}")
print(f"Final Balance = ${balance:.2f}")
# Tells you how much money made/lost to make testing easier


if balance > 100:
    print(f"you made ${balance - TEST_AMOUNT}!")
elif balance < 100:
    print(f"you lost ${balance - TEST_AMOUNT} :(")
