from tkinter import *
import math
root = Tk()
# Script
global num1, num2, operatorValue, result, num1Inputed
num1Inputed = False
result = "" 
num1 = ""
num2 = ""
operatorValue = ""
def putOne():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "1"
        print(num1)
    else:
        num2 = num2 + "1"
        print(num2)
    result = ""


def putZero():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "0"
        print(num1)
    else:
        num2 = num2 + "0"
        print(num2)
    result = ""


def putOne():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "1"
        print(num1)
    else:
        num2 = num2 + "1"
        print(num2)
    result = ""

def putTwo():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "2"
        print(num1)
    else:
        num2 = num2 + "2"
        print(num2)
    result = ""
  
def putThree():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "3"
        print(num1)
    else:
        num2 = num2 + "3"
        print(num2)
    result = ""
  
def putFour():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "4"
        print(num1)
    else:
        num2 = num2 + "4"
        print(num2)
    result = ""
  
def putFive():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "5"
        print(num1)
    else:
        num2 = num2 + "5"
        print(num2)
    result = ""
  
def putSix():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "6"
        print(num1)
    else:
        num2 = num2 + "6"
        print(num2)
    result = ""
  
def putSeven():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "7"
        print(num1)
    else:
        num2 = num2 + "7"
        print(num2)
    result = ""
  
def putEight():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "8"
        print(num1)
    else:
        num2 = num2 + "8"
        print(num2)
    result = ""
  
def putNine():
    global num1, num2, result
    print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "9"
        print(num1)
    else:
        num2 = num2 + "9"
        print(num2)
    result = ""
  
def putDot():
    global num1, num2, result
    print(num1Inputed)
    hasDot = False
    if num1Inputed == False:
        for x in num1:
            if x == ".":
                hasDot = True
        if hasDot == False:
            num1 = num1 + "."
        print(num1)
    else:
        for x in num2:
            if x == ".":
                hasDot = True
        if hasDot == False:
            num2 = num2 + "."
        print(num2)
    result = ""
  
          
def addition():
    global num1, operatorValue, num1Inputed
    print(num1Inputed)
    if num1 != "":
        operatorValue = "addition"
        num1Inputed = True

def equationFinish():
    global num1, num2, operatorValue, result, num1Inputed
    print(num1Inputed)
    if num1 != "" and num2 != "" and operatorValue != "":
        if operatorValue == "addition":
            result = float(num1) + float(num2)
            num1, num2, operatorValue = "", "", ""
            num1Inputed = False
            print(result)





putOne()
putTwo()
putDot()
putOne()






# Interface

# 1
btn1 = Button(root, text="1", command = putOne, width=5, height=1).place(anchor=CENTER, relx=0.1, rely=0.6)

# Addition
btnAdd = Button(root, text="+", command = addition, width=5, height=1).place(anchor=CENTER, relx=0.5, rely=0.6)

# Equal
btnAdd = Button(root, text="=", command = equationFinish, width=5, height=1).place(anchor=CENTER, relx=0.7, rely=0.6)






















root.mainloop()