import random
import sys
import os
import time

def hello():
    print("Hello! Let's play a game where you have to guess the numer from 1 to 10, that have been chosen by the computer.")

def numberHigherLower():
    hello()
    clear = lambda: os.system('clear')
    randomNumber = random.randint(1, 10)
    tries = 0
    while True:
        try:
            userGuess = int(input("Enter a guess between 1 to 10 \n"))
            tries += 1
            if userGuess < randomNumber:
                print("Too low")
            elif userGuess > randomNumber:
                print("Too high")
            else:
                print("Right!")
                print("You took only " + str(tries) + " tries!")
                playAgain=input("Type 'yes' if you want to try again, or type anything else to stop \n").lower()
                if playAgain == "yes":
                    clear()
                    numberHigherLower()
                else:
                    sys.exit(0)
        except ValueError:
            print("This is not a number!")
            time.sleep(2)
            clear()

numberHigherLower()
