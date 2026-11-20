import random

print("DICE SIMULATOR")
while True:
    choice = input("Do you want to roll the dice? (yes/no): ")
    if choice.lower() == "yes":
        number = random.randint(1, 6)
        print("You rolled:", number)
    elif choice.lower() == "no":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. Please enter yes or no.")
