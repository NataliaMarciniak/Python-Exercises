import sys
import random
import time
import os

clear = lambda: os.system('clear')

def hello():
    print("Hello! Welcome to game Rock Paper Scissors. Follow the instructions.")

def tryAgain():
    tryAgain=input("Type 'yes' if You want to play again, or type anything else to stop \n").lower()
    if tryAgain == "yes":
        clear()
        rockPaperScissors()
    else:
        sys.exit(0)

def rockPaperScissors():
    hello()
    time.sleep(0.5)

    while True:
        try:
            userChoice = int(input("Choose the number 1,2 or 3 (1 = paper,2 = rock,3 = scissors) \n"))
            compChoice = random.randrange(1, 3)
            if userChoice == exit:
                sys.exit(0)
            print("3..")
            time.sleep(0.5)
            print("2..")
            time.sleep(0.5)
            print("1..")
            time.sleep(0.5)

            if userChoice == 1 and compChoice == 1:
                print("paper vs paper")
                time.sleep(0.5)
                print("Remis!")
                tryAgain()

            elif userChoice == 2 and compChoice == 2:
                print("rock vs rock")
                time.sleep(0.5)
                print("Remis!")
                tryAgain()
            elif userChoice == 3 and compChoice == 3:
                print("scissors vs scissors")
                time.sleep(0.5)
                print("Remis!")
                tryAgain()

            elif userChoice == 1 and compChoice == 2:
                print("paper vs rock")
                time.sleep(0.5)
                print("You win!")
                tryAgain()
            elif userChoice == 2 and compChoice == 3:
                print("rock vs scissors")
                time.sleep(0.5)
                print("You win!")
                tryAgain()
            elif userChoice == 3 and compChoice == 1:
                print("scissors vs paper")
                time.sleep(0.5)
                print("You win!")
                tryAgain()

            elif userChoice == 1 and compChoice == 3:
                print("paper vs scissors")
                time.sleep(0.5)
                print("You loose!")
                tryAgain()
            elif userChoice == 2 and compChoice == 1:
                print("rock vs paper")
                time.sleep(0.5)
                print("You loose!")
                tryAgain()
            elif userChoice == 3 and compChoice == 2:
                print("scissors vs rock")
                time.sleep(0.5)
                print("You loose!")
                tryAgain()
            else:
                print("Wrong number")
                rockPaperScissors()
        except ValueError:
            print("This is not right choice!")
            time.sleep(2)
            clear()
            tryAgain()

rockPaperScissors()
