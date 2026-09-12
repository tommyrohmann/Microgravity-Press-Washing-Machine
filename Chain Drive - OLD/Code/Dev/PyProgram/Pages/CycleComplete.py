import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class CycleComplete(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tb.Label(self, text="CycleComplete", font=("Helvetica", 8)).pack(pady=30)
        tb.Button(self, text="Back to Home",
                   command=lambda: controller.show_frame("HomePage"),
                   bootstyle=SECONDARY).pack(pady=10)