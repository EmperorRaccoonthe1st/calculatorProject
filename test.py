from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")

var1 = StringVar()
var1.set("hgjhgjhgjhgjhg")

# Frame
blueStyle = ttk.Style().configure("blue.TFrame", background="light blue", borderwidth=5, relief="groove")
mainframe = ttk.Frame(root, padding="2i, 3i", s b tyle="blue.TFrame")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Labels
label1 = Label(mainframe, text="Heyyy", background="forest green")
label2 = Label(mainframe, textvariable=var1.get(), background="dark red")
label1.grid(column=0, row=2)
label2.grid(column=1, row=0)
















root.mainloop()