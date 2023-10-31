from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Sevesoft Clock")

def time():
    string = strftime("%H:%M:%S")
    string2 = strftime("%A %d.%m.%Y")

    label.config(text=string)
    label2.config(text=string2)

    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor="center")

label2 = Label(root, font=("Comic Sans", 34), foreground = "black")
label2.pack(anchor="center")

time()

mainloop()