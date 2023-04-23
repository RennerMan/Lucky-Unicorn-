import random


def generate_token(balance):
    rounds_played = 0
    play_again = ""
    play_again = input("Are you ready to play? (press anything but x to confirm play)")
    while play_again.upper() != "X":
        rounds_played += 1
        number = random.randint(1, 100)
        token = ""
        if 1 <= number <= 5:
            token = "Unicorn"
            balance += 4
        elif 6 <= number <= 36:
            token = "Donkey"
            balance -= 1
        elif number % 2 == 0:
            token = "Horse"
            balance -= 0.5
        else:
            token = "Zebra"
            balance -= 0.5

        print(f"Token: {token}. Balance: {balance:.2f}")

        # Check if balance is enough to continue playing
        if balance < 1:
            print("You ran out of money!")
            play_again = "X"
        else:
            play_again = input("Do you want to play again? Input X to exit or anything else to continue: ")
            print()

    return balance


# Set starting balance and test amount
STARTING_BALANCE = 5


# Call the function and update balance
closing_balance = generate_token(STARTING_BALANCE)

# Print final balance and profit/loss
print(f"Starting Balance = ${STARTING_BALANCE:.2f}")
print(f"Final Balance = ${closing_balance:.2f}")

if closing_balance > STARTING_BALANCE:
    print(f"You made ${closing_balance- STARTING_BALANCE:.2f}!")
elif closing_balance < STARTING_BALANCE:
    print(f"You lost ${STARTING_BALANCE - closing_balance:.2f} :(")
else:
    print("You didn't win or lose any money.")
