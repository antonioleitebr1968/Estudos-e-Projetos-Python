from tkinter import *
class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.button1 = Button(self.myContainer1)
        self.button1.configure(text="OK", background= "green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force() ### (0)
        self.button1.bind("<Return>", self.button1Click)
        self.button1.bind("<Return>", self.button1Click) ### (1)
        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Cancel", background="red")
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Return>", self.button2Click)
    def button1Click(self, event):
        self.report_event(event) ### (3)
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
    def button2Click(self, event):
        report_event(event) ### (4)
        self.myParent.destroy()
    def report_event(self, event): ### (5)
        """Imprime a descrição de um evento, baseado em seus atributos.
        """
        event_name = {"2": "KeyPress", "4": "ButtonPress"}
        print("Time:", str(event.time))### (6)
        print("EventType=" +
              str(event.type),
              event_name[str(event.type)],
              "EventWidgetId=" + str(event.widget),
              "EventKeySymbol=" + str(event.keysym))
root = Tk()
myapp = MyApp(root)
root.mainloop()