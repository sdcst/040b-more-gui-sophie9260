import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")

p = tk.Label(window, text = "Principal")
ir =tk.Label(window, text = "Interest Rate")
y =tk.Label(window, text = "Years")

b1 = tk.Entry(window, text="box 1")
b2 = tk.Entry(window, text="box 2")
b3 = ttk.Combobox(window,values=["1","2","3"])

m = tk.Label(window, text = "-")
a = tk.Label(window, text="Amount")

b4 = tk.Entry(window, text= "Entry")

p.grid(row=1, column=1)
ir.grid(row=1, column=2)
y.grid(row=1, column=3)
b1.grid(row=2, column=1)
b2.grid(row=2,column=2)
b3.grid(row=2, column=3)
m.grid(row=3, column=1)
a.grid(row=4, column=1, sticky=E)
b4.grid(row=4, column=2)

window.mainloop()