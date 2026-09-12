#Import Libraries
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
#Import Modules
if __name__ == "__main__": #allows for editing and local run, otherwise accomodates file structure
    import os, sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modules.InitialStart import Config
from Modules.MachineFunctions import CycleConfigInter

"""Imports Complete beyond this point"""

class CycleSelect(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tb.Label(self, text="CycleSelect", font=("Helvetica", 8)).pack(pady=30)
        tb.Button(self, text="Back to Home",
                   command=lambda: controller.show_frame("HomePage"),
                   bootstyle=SECONDARY).pack(pady=10)

        # Cycle Options
        Cycle_Select_Menu_Button = tb.Menubutton(self, text="Select Cycle", bootstyle=INFO)
        Cycle_Select_Menu_Button.pack(pady=10)

        Cycle_Select_Drop_Menu = tb.Menu(Cycle_Select_Menu_Button, tearoff=0)

        for x in Config.CycleOptions:
            Cycle_Select_Drop_Menu.add_radiobutton(
                label=x,
                command=lambda x=x: self.ChangeCycleOption(x)
            )

        Cycle_Select_Menu_Button["menu"] = Cycle_Select_Drop_Menu

        #Modifier Options
        Modifier_Select_Menu_Button = tb.Menubutton(self, text="Select Modifier", bootstyle=INFO)
        Modifier_Select_Menu_Button.pack(pady=10)

        Modifier_Select_Drop_Menu = tb.Menu(Modifier_Select_Menu_Button, tearoff=0)

        for x in Config.ModifierOptions:
            Modifier_Select_Drop_Menu.add_radiobutton(
                label=x,
                command=lambda x=x: self.ChangeModifierOption(x)
            )

        Modifier_Select_Menu_Button["menu"] = Modifier_Select_Drop_Menu

        # Display Selection Labels
        self.Selected_Cycle_Label = tb.Label(self, text=Config.CycleSelection["Cycle"], font=("Helvetica", 8))
        self.Selected_Cycle_Label.pack(pady=30)
        self.Selected_Modifier_Label = tb.Label(self, text=Config.CycleSelection["Cycle"], font=("Helvetica", 8))
        self.Selected_Modifier_Label.pack(pady=5)

    def ChangeCycleOption(self, option):
        Config.CycleSelection["Cycle"] = option
        print(f"Selected Cycle: {Config.CycleSelection['Cycle']}")  # debug
        self.Selected_Cycle_Label.config(text=Config.CycleSelection["Cycle"])

    def ChangeModifierOption(self, option):
        Config.CycleSelection["Modifier"] = option
        print(f"Selected Modifier: {Config.CycleSelection['Modifier']}")  # debug
        self.Selected_Modifier_Label.config(text=Config.CycleSelection["Modifier"])
