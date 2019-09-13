import tkinter as tk
root = tk.Tk()
root.geometry("400x400")

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()
