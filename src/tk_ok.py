""" Simple Tk program with OK button """
from tkinter import Tk, BOTH, RIGHT, RAISED
# tkinter in pyton 3.x, TKinter in python 2.x
# import tkinter.ttk in python 3.x, import ttk in Python 2.x
# Constants are usually just string word of itself.
# Oddly, all but tkinter.READABLE and tkinter.WRITABLE are repeated
# in tkinter.constants
# Tk is the root window, Frame is a container
# tkinter.Frame != tkinter.ttk.Frame.  For example ttk has no background attribute
from tkinter.ttk import Frame, Button, Style


class Example(Frame):
    # subclase Frame, this is a container.
    def __init__(self, parent):
        # create frame within parent
        Frame.__init__(self, parent)
        # call superclass initializer
        self.parent = parent  # parent window
        self.initUI()

    def initUI(self):
        self.parent.title("Press OK when done")
        # Set root window title

        self.style = Style()
        self.style.theme_use("default")
        # styles

        # frame = Frame(self, relief=RAISED, borderwidth=1)
        frame = Frame(self)
        frame.pack(fill=BOTH, expand=1)
        # this frame has nothing, but pushes buttons down

        self.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
        self.pack(fill=BOTH, expand=1)
        # pack geometry manager with expand in both directions

def main():
    print("Running")
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()
    print("Ran.")

if __name__ == "__main__":
    main()
