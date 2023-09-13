# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]
options_names = {
    "r": "Rock"
    , "p": "Paper"
    , "s": "Scissors"
}

ret = "y"
while ret.lower()=="y":
    # Computer Selection
    computer_choice = random.choice(options)

    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    # Run Conditionals
    print(f"You chose {options_names[user_choice]}. The computer chose {options_names[computer_choice]}.")
    if user_choice==computer_choice:
        print("A smashing tie!")
    elif (user_choice == "r" and computer_choice == "s") \
            or (user_choice == "p" and computer_choice == "r") \
            or (user_choice == "s" and computer_choice == "p"):
        print("Yay! You won.")
    elif (user_choice == "r" and computer_choice == "p") or (user_choice == "p" and computer_choice == "s") or (user_choice == "s" and computer_choice == "r"):
        print("Sorry. You lose.")
    else:
        print("I don't understand that!")
        print("Next time, choose from 'r', 'p', or 's'.")
    ret = input("Do you want to continue? ")
