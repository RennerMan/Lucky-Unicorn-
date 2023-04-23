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
show_instructions = yes_no("Have you played this game before?")
print(f"You entered {show_instructions}")
print()
having_fun = yes_no("are you having fun?")
print(f"You entered {having_fun}")
