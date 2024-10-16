import tkinter as tk
from tkinter import ttk

class GUI(tk.Tk):
    def __init__(self,title,size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}') #For Developement, screen resolution for washing machine
        self.resizable(False,False)
        def close_window(event):
            self.destroy()
        self.bind('<Escape>', close_window)

        self.mainloop()

GUI("Microgravity Press Washing Machine GUI", (800,480))