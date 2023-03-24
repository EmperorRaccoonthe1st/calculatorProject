from tkinter import *
import math
root = Tk()
# Script
num = []
def putOne():
    num.append("1")
    print(num)










# Interface
label1 = Label(root, text="Label", width=20, height=20, font=("calibri bold", 20)).place(anchor=CENTER, relx=0.5, rely=0.5)
btn1 = Button(root, text="1", command = putOne, width=20, height=3).place(anchor=CENTER, relx=0.5, rely=0.6)





















root.mainloop()