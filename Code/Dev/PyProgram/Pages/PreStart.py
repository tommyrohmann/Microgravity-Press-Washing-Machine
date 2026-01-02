import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from Modules.InitialStart import Config

class PreStart(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        Container = tb.Frame(self,bootstyle="warning")
        Container.place(relx=0, rely=0,relwidth=1, relheight=1)

        tb.Label(Container, text="Warning: Ensure clothes loaded and hatch shut\n   Select Proceed to initiat wash cycle", style='warning.inverse.TLabel',font=("Helvetica", 12, "bold")).pack(pady=30)
        tb.Button(Container, text="Proceed",
                   command=lambda: controller.show_frame("WashDashboard"),
                   bootstyle=SECONDARY).pack(pady=10)
        
        #tb.Label(Container, text="Wash Instructions", font=("Helvetica", 8), style='warning.inverse.TLabel').pack(pady=10)
        tb.Label(Container, text=f"""
                    Selected Wash Cycle
                    Wash Cycle: {Config.CycleSelection['Cycle']}
                    Cycle Modifier: {Config.CycleSelection['Modifier']}\n
                    If you do not wish to run this process
                    return to main menu
                """,
                 font=("Helvetica", 8), style='warning.inverse.TLabel'
                 ).pack(pady=0)
        
        #tb.Label(Container, text="", font=("Helvetica", 8), style='warning.inverse.TLabel').pack(pady=10)

        tb.Button(Container, text="Back to Home",
                   command=lambda: controller.show_frame("HomePage"),
                   bootstyle=SECONDARY).place(anchor="se", relx=.98, rely=.98)