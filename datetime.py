import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime

root = Tk()
root.title('Clock ')

def time():

      string = strftime("Date : %d-%m-%Y \n Time : %H:%M:%S %p")
      label.config(text = string)
      label.after(1000, time)

label = Label(root, font = ("ds-digital", 68), background = "Black", foreground = "Violet", )
label.pack(anchor=CENTER)
time()
mainloop()
