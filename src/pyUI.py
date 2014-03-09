""" PyUI Module for introspection based UI.

The plan is in docs/plan.md.   Additional comments are in docs/log.md or may the
git commit messages. """

from tkinter import Tk, BOTH, RIGHT, RAISED, Label
from tkinter.ttk import Frame, Button, Style

class Simple_label(Frame):
    """ The main frame of widgets under the master window.  This contains a simple label """
    def __init__(self, parent, label):
        # create frame within parent
        Frame.__init__(self, parent)
        # call superclass initializer
        self.parent = parent  # parent window
        self.label = label  # single label to print.
        self.initUI()

    def initUI(self):
        self.parent.title("Press OK when done")
        # Set root window title

        self.style = Style()
        self.style.theme_use("default")
        # styles are 'clam' 'default' 'alt' or 'classic', but so far seem the same

        frame = Frame(self, relief=RAISED, borderwidth=1)
        # frame = Frame(self)
        frame.pack(fill=BOTH, expand=1)
        # this frame has nothing, but pushes buttons down
        label1 = Label(frame, text=self.label)
        label1.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Close", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        # close button is pakced into the self window, with padding
        self.pack(fill=BOTH, expand=1)
        # pack geometry manager with expand in both directions
        # so, one call to pack on the label, one on the button
        # how does ordering of these calls really work?

    def center_main_window(self, width=290, height=150):
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        new_x = (screen_width - width) // 2
        new_y = (screen_height - height) // 2
        self.parent.geometry('{}x{}+{}+{}'.format(width, height, new_x, new_y))

def tk_main(label):
    print("Running")
    root = Tk()
    #root.geometry("250x150+300+300")
    app = Simple_label(root, label)
    app.center_main_window()
    root.mainloop()
    print("Ran.")

def _dialog_stub_numbers(arg):
    print("arg=", arg)
    return {"number1": 5, "number2": 8}

def _dialog_stub_display(arg):
    print("arg=", arg)
    return None

def dialog(arg):
    if type(arg) == str:
        tk_main(arg)  # simple label
    else:
        return _dialog_stub_numbers(arg)

if __name__ == "__main__":
    print("You are trying to run the module.")
    print("This should have 'doctor' self-test or demo mode.")
