import sys
import random
import os
import time

def hello():
  print("Hi there, try to guess the number in one try. Good Luck!!!")

def guessTheNumber():
  hello()
  clear = lambda: os.system('clear')
  randomNumber = random.randrange(1,10)
  while True:
    try:
      userGuessedNumber = int(input("Choose your integer from 1 to 10: "))
      if userGuessedNumber == randomNumber:
        print ("Congratulation! You guessed!")
        tryAgain=input("Type 'yes' if You want guess the number again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          guessTheNumber()
        else:
          sys.exit(0)
      elif userGuessedNumber < randomNumber:
        print ("Your number is too small")
        tryAgain=input("Type 'yes' if You want guess the number again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          guessTheNumber()
        else:
          sys.exit(0)
      elif userGuessedNumber > randomNumber:
        print ("Your number is too big")
        tryAgain=input("Type 'yes' if You want guess the number again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          guessTheNumber()
        else:
          sys.exit(0)
      else:
        print ("Wrong input!")
        tryAgain=input("Type 'yes' if You want guess the number again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          guessTheNumber()
        else:
          sys.exit(0)
    except ValueError:
      print("This is not a number!")
      time.sleep(2)
      clear()

guessTheNumber()