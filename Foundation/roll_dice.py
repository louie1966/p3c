import random
roll = random.randint(1, 6)
guess = int(input("Guess a number between 1 and 6:\n"))
if guess == roll:
    print("You guessed it!")
else:
    print(f"You lose,\nyou guessed {guess} and the computer rolled {roll}.")