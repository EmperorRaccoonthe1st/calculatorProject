from tkinter import *
import math
root = Tk()
# Script
global num
num = ""
numList = []
def putOne():
    global num
    num = num + "1"
    print(num)
    
def addition():
    global num
    if num != "":
        print(num)
        numList.append(int(num))
        num = ""
        print(numList)
        
        










# Interface

# 1
btn1 = Button(root, text="1", command = putOne, width=10, height=3).place(anchor=CENTER, relx=0.1, rely=0.6)

# Add
btnAdd = Button(root, text="+", command = addition, width=10, height=3).place(anchor=CENTER, relx=0.5, rely=0.6)






















root.mainloop()