import time
import os
import sys

clear = lambda: os.system('clear')

def hello():
  print("Hello. Let's see if you can build the triangle with sides lenghts that you provide.")
  time.sleep(2)

def chooseTheLenght():
  hello()
  print ("Will it become a triangle? Write: ")
  while True:
    try:
      triangleSideA = int(input("Side lenght a: "))
      try:
        triangleSideB = int(input("Side lenght b: "))
        try:
          triangleSideC = int(input("Side lenght c: "))

          if triangleSideA < triangleSideB:
            temp = triangleSideA
            triangleSideA = triangleSideB
            triangleSideB = temp 
          if triangleSideA < triangleSideC:
            temp = triangleSideA
            triangleSideA = triangleSideC
            triangleSideC = temp
          if triangleSideB < triangleSideC:
            temp = triangleSideB
            triangleSideB = triangleSideC
            triangleSideC =temp
            print (triangleSideA, triangleSideB, triangleSideC)
          if (triangleSideB + triangleSideC) >= triangleSideA:
            print("It becomes a triangle!")
            buildAgain=input("Type 'yes' if You want to check sides of a triangle again, or type anything else to stop \n").lower()
            if buildAgain == "yes":
              clear()
              chooseTheLenght()
            else:
              sys.exit(0)
          else: 
            print("The sides of the triangle are too short!")
            buildAgain=input("Type 'yes' if You want to check sides of a triangle again, or type anything else to stop \n").lower()
            if buildAgain == "yes":
              clear()
              chooseTheLenght()
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
    except ValueError:
        print("This is not a number!")
        time.sleep(2)
        clear()
          
chooseTheLenght()

