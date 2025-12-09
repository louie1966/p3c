import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win! Rock crushes scissors.")
    else:
        print("You lose! Paper covers rock.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win! Paper covers rock.")
    else:
        print("You lose! Scissors cut paper.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! Scissors cut paper.")
    else:
        print("You lose! Rock crushes scissors.")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")
        
    