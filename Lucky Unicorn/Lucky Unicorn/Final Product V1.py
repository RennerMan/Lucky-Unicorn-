# Setting Up formatter to use throughout the code


import random


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides}{text}{sides}"
    top_bottom = symbol * len(formatted_text)
    return f" {top_bottom}\n {formatted_text}\n {top_bottom}"


# Setting Up yes/no function to ensure program doesn't crash


def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
        else:
            print("Please enter either yes or no")


print(formatter("-", "Welcome To the Lucky Unicorn Game!"))
show_instructions = yes_no("Have you played this game before?")
print(f"You entered {show_instructions}")


# Setting Up Instructions


def instructions():
    print()
    print(formatter("*", "Instructions:"))
    print()
    print("You choose a starting amount between 1 and 10 to play with")
    print()
    print("You then press <Enter> to play. Each round costs $1.")
    print()
    print("You have a random chance of getting a Unicorn, a Donkey, a Horse, or a Zebra. ")
    print()
    print("A Unicorn gives you $4, A Donkey loses  you $1, and both a Horse and Zebra loses $0.5.")
    print()
    print("Depending on your luck, you may exit with more than you entered with.")
    print()
    print(formatter("$", "Good Luck!"))


if show_instructions == "No" or show_instructions == "N":
    print(instructions())


# Component 3: (how much v1) -Ask user the amount they want to play with and check their balance is an integer

def num_check(question, low, high):
    error = "That wasn't valid\n" \
            "Please enter a whole number between {} and {}\n".format(low, high)
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


user_balance = num_check("How much would you like to play with?\n (It must be between 1 and 10) $", 1, 10)
print(f"You are playing with ${user_balance}")
input("press <Enter> to play")

# Random Animal Token Generator


balance = user_balance
play_again = ""
token = ""
number = ""
while play_again != "x" and balance != 0:
    for item in range(6):
        number = random.randint(1, 100)

    # Calculate balance based on tokens generated

    if 1 <= number <= 5:
        token = "Unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "Donkey"
        balance -= 1
    else:
        if number % 2 == 0:
            token = "Horse"
            balance -= .5
        else:
            token = "Zebra"
            balance -= .5
    if token != "Unicorn":
        print(f"Token: {token} Balance: {balance: .2f}")
    else:
        print(formatter("!", "Congrats, You got a Unicorn!"))
        print(f"Balance: {balance}")
    play_again = input("Do you want to play again? (press anything but x to continue)")


def statistics():
    print(f"Starting Balance = ${user_balance:.2f}")
    print(f"Final Balance = ${balance:.2f}")
    if balance > user_balance:
        print(f"you made ${balance - user_balance}!")
    else:
        print(f"you lost ${balance - user_balance} :(")


if balance == 0:
    print("You ran out of Money!")
    print(statistics())
    print(formatter("*", "Goodbye!"))
if play_again == "x".lower():
    print("You quit!")
    print(statistics())
    print(formatter("x", "Goodbye!"))
