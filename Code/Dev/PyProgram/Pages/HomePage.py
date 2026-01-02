#Import Libraries
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
#Import Modules
if __name__ == "__main__": #allows for editing and local run, otherwise accomodates file structure
    import os, sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modules.InitialStart import Config
#from Modules.MachineFunctions import 
"""Imports Complete beyond this point"""


a="heyo"
print(a)
print(Config.CycleSelection["Cycle"])

class HomePage(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        

        #Frame Layout
        F_Display = tb.Frame(self,bootstyle="bg") #,relwidth=0.5, relheight=1, Anchor="ne"
        F_Display.place(relx=1/3, rely=0,relwidth=2/3, relheight=1)
        F_SideBar = tb.Frame(self,bootstyle="dark") #,relwidth=0.5, relheight=1, Anchor="ne"
        F_SideBar.place(relx=0, rely=0,relwidth=1/3, relheight=1)

        #Main Display
        B_StartProcess = tb.Button(F_Display, text="Start Process",bootstyle=PRIMARY,
                   command=lambda:
                   controller.show_frame("PreStart"))
        B_StartProcess.place(relx=.5, rely=.5, anchor="center")
        
        D_ProcessSpecs = tb.Label(F_Display, bootstyle="primary",
                                   text=f"Selected Process: {Config.CycleSelection['Cycle']}\nModifier: {Config.CycleSelection['Modifier']}\nSpecifications: NaN", font=("Helvetica", 8))
        D_ProcessSpecs.place(relx=0, rely=1, anchor="sw")

        #Sidebar Menu Items
        Settings_Button = tb.Button(F_SideBar, text="Settings",
                   command=lambda: controller.show_frame("Settings"),
                   bootstyle=SECONDARY).pack(pady=10)
        
        CycleSelect_Button = tb.Button(F_SideBar, text="Cycle Select",
                   command=lambda: controller.show_frame("CycleSelect"),
                   bootstyle=SECONDARY).pack(pady=10)
        
        ViewWashData_Button = tb.Button(F_SideBar, text="View Wash Data",
                   command=lambda: controller.show_frame("ViewWashData"),
                   bootstyle=SECONDARY).pack(pady=10)