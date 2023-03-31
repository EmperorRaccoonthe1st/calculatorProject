from tkinter import *
from tkinter import ttk
import math
root = Tk()
root.title("Calculator")
# Script
global num1, num2, operatorValue, result, num1Inputed, saveNum, nextInput
displayVar = StringVar()
num1Inputed = False
saveNum = False
nextInput = False
result = ""
num1 = ""
num2 = ""
operatorValue = ""
while saveNum == True:
    num1Inputed = True
    nextInput = False


def putZero():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "0"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "0"
        print(num2)
        displayVar.set(num2)
    result = ""


def putOne():
    global num1, num2, result, saveNum, nextInput
    #print(num1Inputed)
    print("nextInput", nextInput, "saveNum", saveNum)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "1"
        print("num1", num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "1"
        print("num2", num2)
        displayVar.set(num2)
    result = ""

def putTwo():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "2"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "2"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putThree():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "3"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "3"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putFour():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "4"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "4"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putFive():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "5"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "5"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putSix():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "6"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "6"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putSeven():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "7"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "7"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putEight():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "8"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "8"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putNine():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    if nextInput == True:
        nextInput = False
        num1 = ""
    if num1Inputed == False:
        num1 = num1 + "9"
        print(num1)
        displayVar.set(num1)
    else:
        num2 = num2 + "9"
        print(num2)
        displayVar.set(num2)
    result = ""
  
def putDot():
    global num1, num2, result, saveNum, nextInput
    # print(num1Inputed)
    hasDot = False
    if nextInput == False:
        if num1Inputed == False:
            for x in num1:
                if x == ".":
                    hasDot = True
            if hasDot == False:
                num1 = num1 + "."
            displayVar.set(num1)
            print(num1)
        else:
            for x in num2:
                if x == ".":
                    hasDot = True
            if hasDot == False:
                num2 = num2 + "."
            displayVar.set(num2)
            print(num2)
        result = ""


def putFlip():
    global num1, num2, num1Inputed, saveNum, nextInput
    print("nextInput", nextInput)
    #if nextInput == True:
     #   nextInput = False
      #  num1 = ""
    if str(num1) != "":
        if str(num1) != "0.0":
            print(num1, num1Inputed)
            if num1Inputed == False:
                print(float(num1))
                if float(num1) > 0:
                    # print(num1, "bigger")
                    num1 = "-" + num1
                    displayVar.set(num1)
                    print(num1)
                else:
                    # print(num1, "smaller")
                    num1 = num1.lstrip(num1[0])
                    print(num1)
                    displayVar.set(num1)
            else:
                if float(num2) > 0:
                    # print(num2, "bigger")
                    num2 = "-" + num2
                    displayVar.set(num2)
                    print(num2)
                else:
                    # print(num2, "smaller")
                    num2 = num2.lstrip(num2[0])
                    displayVar.set(num2)
                    print(num2)
          
def addition():
    global num1, operatorValue, num1Inputed, saveNum, nextInput
    print(num1Inputed)
    if num1 != "":
        if operatorValue == "":
            displayVar.set("+")
            nextInput = False
            operatorValue = "addition"
            num1Inputed = True
        print("saveNum", saveNum, "nextInput", nextInput, "num1", num1)


def subtraction():
    global num1, operatorValue, num1Inputed, saveNum, nextInput
    if num1 != "":
        if operatorValue == "":
            displayVar.set("-")
            nextInput = False
            operatorValue = "subtraction"
            num1Inputed = True


def Multiplication():
    global num1, operatorValue, num1Inputed, saveNum, nextInput
    if num1 != "":
        if operatorValue == "":
            displayVar.set("x")
            nextInput = False
            operatorValue = "Multiplication"
            num1Inputed = True

def Divsion():
    global num1, operatorValue, num1Inputed, saveNum, nextInput
    if num1 != "":
        if operatorValue == "":
            displayVar.set("÷")
            nextInput = False
            operatorValue = "Division"
            num1Inputed = True

def equationFinish():
    global num1, num2, operatorValue, result, num1Inputed, saveNum, nextInput
    print(num1Inputed)
    print(num1, num2, operatorValue)
    if num1 != "" and num2 != "" and operatorValue != "":
        if operatorValue == "addition":
            result = float(num1) + float(num2)
            operatorValue = ""
            num2 = ""
            num1Inputed = False
            num1 = str(result)
            nextInput = True
            displayVar.set(result)
            print("new num1", num1)
            print("result", result)
        elif operatorValue == "subtraction":
            result = float(num1) - float(num2)
            operatorValue = ""
            num2 = ""
            num1Inputed = False
            num1 = str(result)
            nextInput = True
            displayVar.set(result)
            print("new num1", num1)
            print("result", result)
        elif operatorValue == "Multiplication":
            result = float(num1) * float(num2)
            operatorValue = ""
            num2 = ""
            num1Inputed = False
            num1 = str(result)
            nextInput = True
            displayVar.set(result)
            print("new num1", num1)
            print("result", result)
        elif operatorValue == "Division":
            if str(num2) != "0":
                result = float(num1) / float(num2)
                operatorValue = ""
                num2 = ""
                num1Inputed = False
                num1 = str(result)
                nextInput = True
                displayVar.set(result)
                print("new num1", num1)
                print("result", result)
            else:
                result = 0.0
                operatorValue = ""
                num2 = ""
                num1Inputed = False
                num1 = str(result)
                nextInput = True
                displayVar.set("Cannot divide by zero😥")
                print("Cannot divide by zero😥")









# Interface

# Frames
mainFrame = ttk.Frame(root, padding="3c, 1c", relief="groove", borderwidth="1p")
mainFrame.grid(column=0, row=2, sticky=W)
displayStyle = ttk.Style()
displayStyle.configure("display.TFrame", background="Light Grey")
displayFrame = ttk.Frame(root, padding="50p, 5p", relief="sunken", style="display.TFrame")
displayFrame.grid(column=0, row=0)
# 0
btn0 = Button(mainFrame, text="0", command = putZero, width=5, height=1).grid(column=1, row=4)

# 1
btn1 = Button(mainFrame, text="1", command = putOne, width=5, height=1).grid(column=1, row=1, sticky=W)
# 2
btn2 = Button(mainFrame, text="2", command = putTwo, width=5, height=1).grid(column=2, row=1, sticky=W)

# 3
btn3 = Button(mainFrame, text="3", command = putThree, width=5, height=1).grid(column=3, row=1, sticky=W)

# 4
btn4 = Button(mainFrame, text="4", command = putFour, width=5, height=1).grid(column=1, row=2, sticky=W)

# 5
btn5 = Button(mainFrame, text="5", command = putFive, width=5, height=1).grid(column=2, row=2, sticky=W)

# 6
btn6 = Button(mainFrame, text="6", command = putSix, width=5, height=1).grid(column=3, row=2, sticky=W)

# 7
btn7 = Button(mainFrame, text="7", command = putSeven, width=5, height=1).grid(column=1, row=3, sticky=W)

# 8
btn8 = Button(mainFrame, text="8", command = putEight, width=5, height=1).grid(column=2, row=3, sticky=W)

# 9
btn9 = Button(mainFrame, text="9", command = putNine, width=5, height=1).grid(column=3, row=3, sticky=W)

# Dot
btnDot = Button(mainFrame, text=".", command = putDot, width=5, height=1).grid(column=2, row=4, sticky=W)

# Flip
btnFlip = Button(mainFrame, text="+/-", command = putFlip, width=5, height=1).grid(column=3, row=4, sticky=W)

# Addition
btnAdd = Button(mainFrame, text="+", command = addition, width=5, height=1).grid(column=4, row=1, sticky=W)

# Subtraction
btnAdd = Button(mainFrame, text="-", command = subtraction, width=5, height=1).grid(column=4, row=2, sticky=W)

# Multiplication
btnAdd = Button(mainFrame, text="x", command = Multiplication, width=5, height=1).grid(column=4, row=3, sticky=W)

# Division
btnAdd = Button(mainFrame, text="÷", command = Divsion, width=5, height=1).grid(column=4, row=4, sticky=W)

# Equal
btnAdd = Button(mainFrame, text="=", command = equationFinish, width=5, height=1).grid(column=4, row=5, sticky=W)



#displayVar.set()
displayLabelStyle = ttk.Style()
displayLabelStyle.configure("display.TLabel", background="Light Grey")
display = ttk.Label(displayFrame, textvariable=displayVar, style="display.TLabel").grid(column=1, row=0)






















root.mainloop()