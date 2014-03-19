
""" Add two numbers with an OK and layout. """

import tkinter as tk
import tkinter.ttk as ttk

def get_numbers():
    values = {}
    self.root = tk.Tk()
    self.main = tk.Frame(self.root)
    self.root.title("Add Two")

    self.content_frame = tk.Frame(self.root, relief=RAISED, borderwidth=1)
    self.label1 = tk.Label(self.content_frame, text="Enter first xnumber:").grid(row=0)
    self.label2 = tk.Label(self.content_frame, text="Enter second number:").grid(row=1)
    self.entry1 = tk.Entry(self.content_frame).grid(row=0, col=1)
    self.entry2 = tk.Entry(self.content_frame).grid(row=1, col=0)

    self.ok = tk.Button(self.main, text="OK")
    self.cancel = tk.Button(self.main, text="Cancel")
    self.main.pack(fill=BOTH, expand=1)
    self.root.mainloop()
