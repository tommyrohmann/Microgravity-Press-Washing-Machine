import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class HaltProcess(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        Abort_Button = tb.Button(self, text="Abort Process",
                   command=lambda: controller.show_frame("CycleComplete"),
                   bootstyle=SECONDARY).pack(pady=10)
        
        Resume_Button = tb.Button(self, text="Resume Process",
                   command=lambda: controller.show_frame("WashDashboard"),
                   bootstyle=SECONDARY).pack(pady=10)