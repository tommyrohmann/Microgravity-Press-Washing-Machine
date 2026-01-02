import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from Modules.InitialStart import Config

class Settings(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tb.Label(self, text="Settings", font=("Helvetica", 8)).pack(pady=30)
        tb.Button(self, text="Back to Home",
                   command=lambda: controller.show_frame("HomePage"),
                   bootstyle=SECONDARY).place(anchor="se", relx=.98, rely=.98)
        

        tb.Label(self, text=f"Default Wash Process: {Config.BootData['DefaultWashProcess']}", font=("Helvetica", 8)).pack(pady=0)
        tb.Label(self, text=f"Default Wash Modifier: {Config.BootData['DefaultWashModifier']}", font=("Helvetica", 8)).pack(pady=0)
        
        tb.Label(self, text=f"Machine Info", font=("Helvetica", 8)).pack(pady=10)
        tb.Label(self, text=f"Run Hours: {Config.BootData['RunHours']}", font=("Helvetica", 8)).pack(pady=0)
        tb.Label(self, text=f"Wash Count: {Config.BootData['WashCount']}", font=("Helvetica", 8)).pack(pady=0)
        
        #tb.Label(self, text=f"Wash Data Sample Frequency: {Config.BootData['DataRecordResolution(ms)']}", font=("Helvetica", 8)).pack(pady=10)