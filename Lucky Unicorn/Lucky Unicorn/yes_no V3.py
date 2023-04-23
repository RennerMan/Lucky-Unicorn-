show_instructions = ""
while show_instructions != "x":
    show_instructions = input("have you played this game before?").lower()
    if show_instructions == "yes" or show_instructions == "y":
        print("Program Continues")
        elif show_instructions == "no" or show_instructions == "n":
            print("Show Instructions")
        else:
        print("Please enter either yes or no")

    print(f"You entered {show_instructions}")
