# Component 3: (how much v1) -Ask user the amount they want to play with and check their balance is an integer
# between 1 and 10.


balance = int(input("How much money do you want to play with? (1-10)"))
while not 1 <= balance <= 10:
    print("please enter a whole amount from 1-10 dollars")
    int(input("How much money do you want to play with? (1-10)"))

print(f"you are playing with {balance} dollars")
