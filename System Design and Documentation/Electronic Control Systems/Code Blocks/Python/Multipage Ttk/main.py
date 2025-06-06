'''
Tommy Rohmann
2-27-2025

Tutorials Used
https://www.w3schools.com/python/python_virtualenv.asp
https://ttkbootstrap.readthedocs.io/en/version-0.5/tutorial.html

Create new theme: python -m ttkcreator

Given the complexity of the project at hand, initial research has been done using chatGPT,
so far it has proven to be an amazing tool for initial research and brainstorming. This is allowing
me to make considerable progress when before I initially find it difficult to pick an approach for
developement. This would be because any given approach has some limitation which would make it a poor choice
for the application I have in mind, even if it would be adequate for an individual piece of the project I
would make as a proof of concept.
'''

import ttkbootstrap as ttk
from ttkbootstrap import Style #Style Library
from page_one import PageOne
from page_two import PageTwo

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
#Window Configuration
        self.title("Multipage App Test with ttkbootstrap") #Page title at top of window
        self.geometry("800x480") #Page Resolution
        self.shared_data = {"name": ttk.StringVar()} #Global Dictionary
        style = Style("solar")

        container = ttk.Frame(self) #fills area with window
        container.pack(fill="both", expand=True)

        self.frames = {} #dictionary sets up page data dictionary for GUI application
        for Page in (PageOne, PageTwo): #For loop cycles through all pages
            page_name = Page.__name__
            frame = Page(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageTwo")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if hasattr(frame, "on_show"):
            frame.on_show()

if __name__ == "__main__":
    app = App()
    app.mainloop()