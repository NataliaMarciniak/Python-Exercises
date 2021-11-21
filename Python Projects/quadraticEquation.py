import os
import sys
import time

def hello():
    print("Hello, this program helps you to find delta in your equation.")

def equationParameterValues():
    hello()
    clear = lambda: os.system('clear')
    print ("For the quadratic equation: ax^2+bx+c=0")
    while True:
        try:
            firstEquationNumber=int(input("Enter the value of the parameter a: "))
            try:
                secondEquationNumber=int(input("Enter the value of the parameter b: "))
                try:
                    thirdEquationNumber=int(input("Enter the value of the parameter c: "))
                    delta = secondEquationNumber**2-4*firstEquationNumber*thirdEquationNumber
                    if delta > 0:
                        distinctRoot1 = (-secondEquationNumber-delta**(1/2))/(2*firstEquationNumber)
                        distinctRoot2 = (-secondEquationNumber+delta**(1/2))/(2*firstEquationNumber)
                        print ('x1 = ', distinctRoot1, ', x2 = ', distinctRoot2)
                        tryAgain=input("Type 'yes' if You want to check sides of a triangle again, or type anything else to stop \n").lower()
                        if tryAgain == "yes":
                            clear()
                            equationParameterValues()
                        else:
                            sys.exit(0)
                    elif delta == 0:
                        realRoot = -secondEquationNumber/(2*firstEquationNumber)
                        print ('x0 = ', realRoot)
                        tryAgain=input("Type 'yes' if You want to check sides of a triangle again, or type anything else to stop \n").lower()
                        if tryAgain == "yes":
                            clear()
                            equationParameterValues()
                        else:
                            sys.exit(0)
                    else:
                        print ("No solutions")
                        tryAgain=input("Type 'yes' if You want to check sides of a triangle again, or type anything else to stop \n").lower()
                        if tryAgain == "yes":
                            clear()
                            equationParameterValues()
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

equationParameterValues()
