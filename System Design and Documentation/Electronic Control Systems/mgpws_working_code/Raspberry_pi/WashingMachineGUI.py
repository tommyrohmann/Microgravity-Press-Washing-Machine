import tkinter as tk
from tkinter import ttk

#window
GUI = tk.Tk()
GUI.title('Microgravity Press Washing Machine GUI')
GUI.geometry('800x480') #For Developement
#GUI.attributes('-fullscreen',True) #Fullscreen for when implemented on machine
#Close Window
def close_window(event):
    GUI.destroy()
GUI.bind('<Escape>', close_window)

#def Operational Functions
def execute_wash_process():
    print("hi")
#pages


#widgets

#run
GUI.mainloop()