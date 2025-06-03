import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = ttk.Label(self, text="", font=("Segoe UI", 12))
        self.label.pack(pady=20)

        ttk.Button(self, text="Back", bootstyle=SECONDARY,
                   command=lambda: controller.show_frame("PageOne")).pack(pady=10)

    def on_show(self):
        name = self.controller.shared_data["name"].get()
        self.label.config(text=f"Hello, {name}!")
