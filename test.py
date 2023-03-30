from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")

global var2
var2 = "Hola"
var1 = StringVar()
var1.set(var2)
def changeVar2 (event):
    global var2
    if var2 == "Hola":
        var2 = "What's Up"
    elif var2 == "What's Up":
        var2 = "Hola"
    print("ran")
# Frame
blueStyle = ttk.Style().configure("blue.TFrame", background="light blue", borderwidth=5, relief="groove")
mainframe = ttk.Frame(root, padding="1i, 1i", style="blue.TFrame")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Labels
label1 = ttk.Label(mainframe, text="Heyyy", background="forest green")
label2 = ttk.Label(mainframe, background="dark red")
label1.grid(column=0, row=2)
label2.grid(column=1, row=0)
root.bind("<Enter>", changeVar2)
while True:
    label2.configure(textvariable=var1)
    break
















root.mainloop()