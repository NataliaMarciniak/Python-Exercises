import sys
import os
import time

clear = lambda: os.system('clear')

def hello():
  print("Hello, You can check here if your number is even or odd.")

def typedNumbers():
  hello()
  while True:
    try:
      userChoice = int(input("Write your number: "))
      if userChoice % 2:
        print("Your number is odd")
        tryAgain=input("Type 'yes' if You want to check your numbers again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          typedNumbers()
        else:
          sys.exit(0)
      else:
        print("Your number is even")
        tryAgain=input("Type 'yes' if You want to check your numbers again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          typedNumbers()
        else:
          sys.exit(0)
    except ValueError:
      print("This is not a number!")
      time.sleep(2)
      clear()

typedNumbers()