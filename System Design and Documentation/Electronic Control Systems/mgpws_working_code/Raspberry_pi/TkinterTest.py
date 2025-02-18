import tkinter as tk

class MyApp(tk.frame):
    def __init__(self, root):
    #Color Pallete: #000000, #888888, #15418C, #428BCA, #FFFFFF, #FC3D21
        self.color1 = "#15418C"
        self.color2 = "#428BCA"
        self.color3 = "white"

        super().__init__(
            root,
            bg=self.color1
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

