from tkinter import *

jan = Tk()
jan.geometry("500x500")
jan.configure(background="#f0f0f0")

head = PhotoImage(file = "imgs\\jaden4.png")
label = Label(jan, image = head)
label.place(x=100 , y=10)


def crt():
   head['file'] = "imgs\\jaden5.png"


crt = Button(jan, text="TROCAR ROSTO", font=("Centurty Gothic",10), command=crt)
crt.place(x=5, y=10)

jan.mainloop()