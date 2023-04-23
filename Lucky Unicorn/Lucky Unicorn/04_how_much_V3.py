# Component 3: (how much v1) -Ask user the amount they want to play with and check their balance is an integer
def num_check(question, low, high):
    error = "That wasn't valid\n"\
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

# main routine


user_balance = num_check("How much would you like to play with?\n (It must be between 1 and 10) $", 1, 10)
print(f"You are playing with ${user_balance}")
