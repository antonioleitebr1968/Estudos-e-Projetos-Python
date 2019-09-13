from tkinter import *
from functools import partial
from time import sleep

root = Tk()

def bg_config(widget, bg, fg, event):
    widget.configure(background=bg, foreground=fg)
    #Fading effect here

btn = Button(root, text="Button", relief=GROOVE, bg="white")

btn.bind("<Enter>", partial(bg_config, btn, "#f47142", "white"))
btn.bind("<Leave>", partial(bg_config, btn, "white", "black"))

btn.pack()
root.mainloop()

