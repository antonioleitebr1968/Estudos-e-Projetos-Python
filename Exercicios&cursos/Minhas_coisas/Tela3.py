from tkinter import *


class ClearApp:
    def __init__(self, parent=0):
        self.mainWindow = Frame(parent)
        # cria um widget caixa de texto
        self.entry = Entry(self.mainWindow)
        self.entry.insert(0, "Hello world")
        self.entry.pack(fill=X)

        # agora adiciona 2 botões
        fOuter = Frame(self.mainWindow, border=1, relief="sunken")
        fButtons = Frame(fOuter, border=1, relief="raised")
        bClear = Button(fButtons, text="Clear",
                        width=8, height=1, command=self.clearText)
        bQuit = Button(fButtons, text="Quit",
                       width=8, height=1, command=self.mainWindow.quit)
        bClear.pack(side="left", padx=15, pady=1)
        bQuit.pack(side="right", padx=15, pady=1)
        fButtons.pack(fill=X)
        fOuter.pack(fill=X)
        self.mainWindow.pack()

        # coloca um titulo
        self.mainWindow.master.title("Clear")

    def clearText(self):
        self.entry.delete(0, END)


app = ClearApp()
app.mainWindow.mainloop()