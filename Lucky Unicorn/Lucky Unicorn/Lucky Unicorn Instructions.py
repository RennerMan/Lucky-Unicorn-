
# Component 2: Yes/No Function
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


# Component 3: Instructions Function
def instructions():
    print("_-_-_How to play_-_-_")
    print()
    print("Here are the rules:")
    print()
    print("program continues")
# Main Routine


played_before = yes_no("Have you played this game before? ")
if played_before == "no" or played_before == "n":
    instructions()
else:
    print("program continues")

