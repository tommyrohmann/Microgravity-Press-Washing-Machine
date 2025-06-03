import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Enter your name:", font=("Segoe UI", 12)).pack(pady=10)

        self.entry = ttk.Entry(self, textvariable=controller.shared_data["name"], width=30)
        self.entry.pack(pady=5)

        ttk.Button(self, text="Continue", bootstyle=SUCCESS,
                   command=self.go_to_next_page).pack(pady=20)

    def go_to_next_page(self):
        name = self.entry.get()
        if name:
            self.controller.shared_data["name"].set(name)
            self.controller.show_frame("PageTwo")