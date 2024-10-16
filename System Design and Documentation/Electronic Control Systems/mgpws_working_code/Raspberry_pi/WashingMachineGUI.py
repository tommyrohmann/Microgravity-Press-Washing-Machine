import tkinter as tk
from tkinter import ttk

page_manager = 1

#window
GUI = tk.Tk()
GUI.title('Microgravity Press Washing Machine GUI')
GUI.geometry('800x480') #For Developement, screen resolution for washing machine
GUI.resizable(False,False)
#GUI.attributes('-fullscreen',True) #Fullscreen for when implemented on machine
#Close Window
def close_window(event):
    GUI.destroy()
GUI.bind('<Escape>', close_window)
#Color Pallete: #000000, #888888, #15418C, #428BCA, #FFFFFF, #FC3D21

#def Operational Functions
def execute_wash_process():
    print("hi")

def gui_manager():
    global open

#Defining Frames
main_page = tk.Frame(GUI,bg="#428BCA")
main_page.pack()
main_page.pack_propagate(False)
main_page.configure(width=800, height=480)

run_button = tk.Button()

def page_update():
    if page_manager == 1: main_page.pack()
    else: main_page.destroy()
    if page_manager == 2: run_page.pack()
    else: run_page.destroy()
    if page_manager == 3: settings_page.pack()
    else: settings_page.destroy()



#run
GUI.mainloop()