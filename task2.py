import random
import time

name = ""  # Define name globally

def intro():
    global name
    print("May I ask you for your name?")
    name = input()
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    number = random.randint(1, 200)  # Generate a new random number for each game
    guessesTaken = 0

    while guessesTaken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)

            if 1 <= guess <= 200:
                guessesTaken += 1
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    else:
                        break
                    time.sleep(0.5)
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200.")

        except ValueError:
            print(f"I don't think that '{enter}' is a number. Sorry.")

    if guess == number:
        print(f'Good job, {name}! You guessed my number in {guessesTaken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {number}.')

playagain = "yes"
while playagain.lower() in ["yes", "y"]:
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()
