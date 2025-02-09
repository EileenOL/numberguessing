import random

def intro():
    print("Welcome my number guessing game. Please guess a number from 1 - 100")

def randomNumber():
    return random.randint(1, 100)

def player():
    guess = input("Enter your guess: ")
    while not guess.isdigit():
        print("Invalid input. Please enter a valid number.")
        guess = input("Enter your guess: ")
    return int(guess)

def guessChecker(playerGuess, actualGuess):
    if playerGuess < actualGuess:
        print("Too low! Try again")
        return False
    elif playerGuess > actualGuess:
        print("Too high! Try again")
        return False
    else:
        print(f"Congratulations! You guessed the correct number: {actualGuess}")
        return True
   
def game():
    intro()
    actualGuess = randomNumber()
    trials = 0

    while True:
        playerGuess = player()
        trials += 1
        if guessChecker(playerGuess, actualGuess):
            print(f"You guessed the correct number in {trials} trials.")
            break
game()


# git init
# git add .
# git branch -M main
# git commit -m first commit
# git remote add origin https://github.com/EileenOL/numberguessing.git
# git push -u origin main