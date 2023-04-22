# Component 1: Setting up Functions
def yes_no(question_text):
    while True:

        # Component 2: Ask user if they have played before
        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            answer = "yes"
        return answer
        elif "No" == answer or answer == "N":
            answer = "No"
        return answer

        else:
        print("please pick either yes or no")
        print(f"You entered '{show_instructions}'")

# Main Routine


question = yes_no("Have you played this game before?")
print(f"You entered '{question}'")

play_round = input("Do you want to play a round?")
import random
tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]


