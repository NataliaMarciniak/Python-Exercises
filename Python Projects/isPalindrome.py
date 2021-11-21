import sys
import os
import time

def hello():
  print("Hello there! You can check here if your word is a palindrome or not. Let's start!")

def palindrome():
  hello()
  clear = lambda: os.system('clear')
  while True:
    userWord = input("Please write your word to check it: ").lower()
    reversedWord = userWord[::-1]
    print (reversedWord)
    if userWord.isnumeric():
      print("This is not a word!")
      time.sleep(2)
      clear()
    else:
      if userWord == reversedWord:
        print("This word is a palindrome")
        tryAgain=input("Type 'yes' if You want to check your word again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          palindrome()
        else:
          sys.exit(0)
      else:
        print("This word is not a palindrome")
        tryAgain=input("Type 'yes' if You want to check your word again, or type anything else to stop \n").lower()
        if tryAgain == "yes":
          clear()
          palindrome()


palindrome()