import sys
import os
import time

def hello():
  print("Welcome to the calculator! Follow the instruction to get your result.")

def calculator():
  hello()
  clear = lambda: os.system('clear')
  while True:
    try:
      firstNumber = int(input("Write the first number: "))
      operation = input("Choose the operation +,-,/,*: ")
      if(operation != "*" and operation != "/" and operation != "-" and operation != "+"):
        print("Wrong operator!")
        time.sleep(2)
        clear()
        calculator()
      while True:
        try:
          secondNumber = int(input("Write the second number: "))
          if operation == "*":
            print(firstNumber * secondNumber)
          elif operation == "/":
            print(firstNumber / secondNumber)
          elif operation == "-":
            print(firstNumber - secondNumber)
          elif operation == "+":
            print(firstNumber + secondNumber)
          else:
            break
          tryAgain=input("Type 'yes' if You want to use the calculator again, or type anything else to stop \n").lower()
          if tryAgain == "yes":
            clear()
            calculator()
          else:
            sys.exit(0)
        except ValueError:
          print("This is not a number!")
          time.sleep(2)
          clear()

    except ValueError:
      print("This is not a number!")
      time.sleep(2)
      clear()  
 


calculator()