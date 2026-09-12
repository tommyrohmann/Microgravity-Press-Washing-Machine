import tkinter as tk
import time

class MultiPageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi Page App with State Machine")

        # Initialize the state
        self.state = "page1"

        # Create a container frame to hold all pages
        self.container = tk.Frame(self.root)
        self.container.pack(expand=True, fill="both")

        # Create pages
        self.page1 = self.create_page1()
        self.page2 = self.create_page2()
        self.page3 = self.create_page3()

        # Display the initial page
        self.show_page()

    def create_page1(self):
        frame = tk.Frame(self.container)
        label = tk.Label(frame, text="This is Page 1")
        label.pack(pady=20)

        btn_to_page2 = tk.Button(frame, text="Go to Page 2", command=lambda: self.transition_to("page2"))
        btn_to_page2.pack(pady=10)

        btn_to_page3 = tk.Button(frame, text="Go to Page 3", command=lambda: self.transition_to("page3"))
        btn_to_page3.pack(pady=10)

        # Add a button to run Python code
        btn_run_code = tk.Button(frame, text="Run Python Code", command=self.run_python_code)
        btn_run_code.pack(pady=10)

        return frame

    def create_page2(self):
        frame = tk.Frame(self.container)
        label = tk.Label(frame, text="This is Page 2")
        label.pack(pady=20)

        btn_to_page1 = tk.Button(frame, text="Go to Page 1", command=lambda: self.transition_to("page1"))
        btn_to_page1.pack(pady=10)

        btn_to_page3 = tk.Button(frame, text="Go to Page 3", command=lambda: self.transition_to("page3"))
        btn_to_page3.pack(pady=10)

        # Add a button to run Python code
        btn_run_code = tk.Button(frame, text="Run Python Code", command=self.run_python_code)
        btn_run_code.pack(pady=10)

        return frame

    def create_page3(self):
        frame = tk.Frame(self.container)
        label = tk.Label(frame, text="This is Page 3")
        label.pack(pady=20)

        btn_to_page1 = tk.Button(frame, text="Go to Page 1", command=lambda: self.transition_to("page1"))
        btn_to_page1.pack(pady=10)

        btn_to_page2 = tk.Button(frame, text="Go to Page 2", command=lambda: self.transition_to("page2"))
        btn_to_page2.pack(pady=10)

        # Add a button to run Python code
        btn_run_code = tk.Button(frame, text="Run Python Code", command=self.run_python_code)
        btn_run_code.pack(pady=10)

        return frame

    def transition_to(self, page):
        self.state = page
        self.show_page()

    def show_page(self):
        # Hide all pages first
        for widget in self.container.winfo_children():
            widget.pack_forget()

        # Display the page based on the current state
        if self.state == "page1":
            self.page1.pack(expand=True, fill="both")
        elif self.state == "page2":
            self.page2.pack(expand=True, fill="both")
        elif self.state == "page3":
            self.page3.pack(expand=True, fill="both")

    def run_python_code(self):
        # Example Python code that runs when the button is pressed
        print("Python code is running!")
        result = self.some_function()
        print(f"Result from function: {result}")
        
        # You can also update the UI based on the code execution
        result_label = tk.Label(self.container, text=f"Code Execution Result: {result}")
        result_label.pack(pady=20)

    def some_function(self):
        # Example function that you might want to run
        time.sleep(1)  # Simulate some processing
        return "Hello, World!"

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiPageApp(root)
    root.mainloop()
