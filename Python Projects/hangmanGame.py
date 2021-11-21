import random
import time
import sys
import os

clear = lambda: os.system('clear')

def hello():
  print("Welcome to Hangman game")
  name = input("Enter your name:   ")
  print("Hello " + name + " Good luck!")
  time.sleep(2)
  print("The game is about to start!")
  time.sleep(3)
  clear()

def hangman():  
  userLives = 10
  baseOfWords = ["puzzle", "radiator","rabbit","kitchen","backpack","window","flower","winter","kettle","honey","tangerine","fridge","balcony","playstation","candle","trousers","spoon","microwave","coffe"]
  randomWord = random.choice(baseOfWords)
  hiddenWord = []
  guessedLetters = []

  hello()
  
  for letter in randomWord:
    hiddenWord.append("_")

  while userLives >= 0:
    print(" ".join(hiddenWord))
    if userLives > 0:
      print("You have " + str(userLives) + " lives")
      print ("Already guessed letters: " + " ".join(guessedLetters))
      try:
        userGuess = input("Guess your letter or try to guess a word: ").lower()
        if userGuess.isnumeric():
          print("This is not a letter!")
          time.sleep(2)
          clear()
        if len(userGuess) > 1:
          if(userGuess == randomWord):
            print("YOU WIN!")
            playAgain=input("Type 'yes' if You want to play again or anything else to stop \n").lower()
            if playAgain == "yes":
              clear()
              hangman()
            else:
              sys.exit(0)
          else:
            print("It's not that word")
        clear()
        isInWordList = []
        for i in range(0,len(randomWord)):
          if userGuess == randomWord[i]:
            isInWordList.append("1")
            hiddenWord[i] = userGuess
          else:
            isInWordList.append("0")
        if userGuess in guessedLetters:
          print("You already guessed this letter")
        if userGuess not in guessedLetters and not userGuess.isnumeric() and len(userGuess) == 1:
          guessedLetters.append(userGuess)
        if "_" not in hiddenWord:
          print("YOU WIN!")
          playAgain=input("Type 'yes' if You want to play again or anything else to stop \n").lower()
          if playAgain == "yes":
            clear()
            hangman()
          else:
            sys.exit(0)
        if "1" not in isInWordList:
          userLives -= 1;  
      except ValueError:
        print("x")
    else:
      print("You lost all your lives.")
      print("GAME OVER")
      print("The word was: " + randomWord)
      playAgain=input("Type 'yes' if You want to play again or anything else to stop \n").lower()
      if playAgain == "yes":
        clear()
        hangman()
      else:
        sys.exit(0)


hangman()

