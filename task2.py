import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("500x530")

pa = tk.Label(window, text = "POKEMON ADVENTURE")

mm = tk.Label(window, text = "MINI MAP")

bigmap = PhotoImage(file="main.png")
image1 = tk.Label(window, image=bigmap)

smallmap = PhotoImage(file = "minimap.png")
image2 = tk.Label(window, image = smallmap)

logo = PhotoImage(file = "logo.png")
image3 = tk.Label(window, image = logo)

map = tk.Button(window, text = "MAP", anchor="center" )
inventory = tk.Button(window, text = "INVENTORY", anchor="center" )
poke = tk.Button(window, text = "POKEDEX", anchor="center" )
roster = tk.Button(window, text = "ROSTER" , anchor="center")
journal = tk.Button(window, text = "JOURNAL", anchor="center")
help = tk.Button(window, text = "HELP", anchor="center" )
shop = tk.Button(window, text = "SHOP", anchor="center")

nw = tk.Button(window, text = "NW" , anchor="center")
n = tk.Button(window, text = "N" , anchor="center")
ne = tk.Button(window, text = "NE" , anchor="center")
e = tk.Button(window, text = "E" , anchor="center")
se = tk.Button(window, text = "SE", anchor="center" )
s = tk.Button(window, text = "S", anchor="center" )
sw = tk.Button(window, text = "SW", anchor="center" )
w = tk.Button(window, text = "W", anchor="center" )

pa.place(x=200, y=10)
mm.place(x=400, y = 80)
image1.place(x=10, y = 40, height=370, width = 370)
image2.place(x=400, y= 100, height = 80, width = 80)
image3.place(x= 200, y = 430)
map.place(x = 400, y = 200,height=30, width = 80)
inventory.place(x = 400, y = 230,height=30, width = 80)
poke.place(x = 400, y = 260,height=30, width = 80)
roster.place(x = 400, y = 290,height=30, width = 80)
journal.place(x = 400, y = 320,height=30, width = 80)
help.place(x = 400, y = 350,height=30, width = 80)
shop.place(x = 400, y = 380,height=30, width = 80)
nw.place(x=10, y=430, height= 30, width = 30 )
n.place(x=40, y=430, height= 30, width = 30 )
ne.place(x=70, y=430, height= 30, width = 30 )
e.place(x=70, y=460, height= 30, width = 30 )
se.place(x=70, y=490, height= 30, width = 30 )
s.place(x=40, y=490, height= 30, width = 30 )
sw.place(x=10, y=490, height= 30, width = 30 )
w.place(x=10, y=460, height= 30, width = 30 )

window.mainloop()