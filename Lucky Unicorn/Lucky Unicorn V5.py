# Component 1: Setting up Functions
import random

def yes_no(question_text):
    while True:
        # Component 2: Ask user if they have played before
        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            return "yes"
        elif answer == "no" or answer == "n":
            return "no"
        else:
            print("Please pick either yes or no")

# Main Routine
question = yes_no("Have you played this game before? ")
print(f"You entered '{question}'")
if question == "no":
    print("Show instructions")
play_round = input("Do you want to play a round? ")
tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]
random_token = random.choice(tokens)
print(f"Your token for this round is: {random_token}")