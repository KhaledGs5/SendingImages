import tkinter as tk
from tkinter import ttk

class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Input Interface")
        self.geometry("300x150")

        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self.label = ttk.Label(self, text="Enter your text:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.text_entry = ttk.Entry(self, font=("Arial", 12))
        self.text_entry.pack(pady=5, padx=20, fill=tk.X)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_text)
        self.submit_button.pack()

    def submit_text(self):
        self.email_to = self.text_entry.get()
        self.destroy()