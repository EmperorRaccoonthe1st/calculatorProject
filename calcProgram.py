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
    # print(num1Inputed)
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
    #print(num1Inputed)
    if num1Inputed == False:
        num1 = num1 + "1"
        print("num1", num1)
    else:
        num2 = num2 + "1"
        print("num2", num2)
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


def putFlip():
    global num1, num2, num1Inputed
    if num1Inputed == False:
        print(float(num1))
        if float(num1) > 0:
            print(num1, "bigger")
            num1 = "-" + num1
            print(num1)
        else:
            print(num1, "smaller")
            num1 = num1.lstrip(num1[0])
            print(num1)
    else:
        if float(num2) > 0:
            print(num2, "bigger")
            num2 = "-" + num2
            print(num2)
        else:
            print(num2, "smaller")
            num2 = num2.lstrip(num2[0])
            print(num2)
          
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










# Interface

# 0
btn0 = Button(root, text="0", command = putZero, width=5, height=1).place(anchor=CENTER, relx=0.1, rely=0.4)

# 1
btn1 = Button(root, text="1", command = putOne, width=5, height=1).place(anchor=CENTER, relx=0.1, rely=0.1)

# 2
btn2 = Button(root, text="2", command = putTwo, width=5, height=1).place(anchor=CENTER, relx=0.2, rely=0.1)

# 3
btn3 = Button(root, text="3", command = putThree, width=5, height=1).place(anchor=CENTER, relx=0.3, rely=0.1)

# 4
btn4 = Button(root, text="4", command = putFour, width=5, height=1).place(anchor=CENTER, relx=0.1, rely=0.2)

# 5
btn5 = Button(root, text="5", command = putFive, width=5, height=1).place(anchor=CENTER, relx=0.2, rely=0.2)

# 6
btn6 = Button(root, text="6", command = putSix, width=5, height=1).place(anchor=CENTER, relx=0.3, rely=0.2)

# 7
btn7 = Button(root, text="7", command = putSeven, width=5, height=1).place(anchor=CENTER, relx=0.1, rely=0.3)

# 8
btn8 = Button(root, text="8", command = putEight, width=5, height=1).place(anchor=CENTER, relx=0.2, rely=0.3)

# 9
btn9 = Button(root, text="9", command = putNine, width=5, height=1).place(anchor=CENTER, relx=0.3, rely=0.3)

# Dot
btnDot = Button(root, text=".", command = putDot, width=5, height=1).place(anchor=CENTER, relx=0.2, rely=0.4)

# Flip
btnFlip = Button(root, text="+/-", command = putFlip, width=5, height=1).place(anchor=CENTER, relx=0.3, rely=0.4)

# Addition
btnAdd = Button(root, text="+", command = addition, width=5, height=1).place(anchor=CENTER, relx=0.4, rely=0.1)

# Equal
btnAdd = Button(root, text="=", command = equationFinish, width=5, height=1).place(anchor=CENTER, relx=0.4, rely=0.4)






















root.mainloop()