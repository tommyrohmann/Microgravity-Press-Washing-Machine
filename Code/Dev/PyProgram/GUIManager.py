import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

#Import pages from other files
from Pages.HomePage import HomePage
from Pages.PreStart import PreStart
from Pages.WashDashboard import WashDashboard
from Pages.HaltProcess import HaltProcess
from Pages.CycleComplete import CycleComplete
from Pages.CycleSelect import CycleSelect
from Pages.Settings import Settings
from Pages.ViewWashData import ViewWashData

#https://www.pythontutorial.net/tkinter/tkinter-place/
#python -m ttkcreator

class GUI(tb.Window):
    def __init__(self):
        super().__init__(title="MGP Washing Machine UI Dashboard", themename='iss',size=(800, 480))
        self.frames = {}
        
        '''Uncomment for icon and fullscreen
        #self.iconbitmap()
        #self.attributes('-fullscreen', True) #Fullscreen Module
        #'''

        # Container to hold all pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.pages = {}  # Dictionary to store page instances
        self.create_pages()

        # Initialize all pages
    def create_pages(self):
        for F in (HomePage, PreStart, WashDashboard, HaltProcess, CycleComplete, CycleSelect, Settings, ViewWashData):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.pages[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Bring the selected page to the front."""
        frame = self.pages[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()