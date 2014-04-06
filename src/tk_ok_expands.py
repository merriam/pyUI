""" Simple Tk program with OK button """
import tkinter as tk
import tkinter.ttk as ttk
import re

import tkinter as tk
# tkinter in pyton 3.x, TKinter in python 2.x
# import tkinter.ttk in python 3.x, import ttk in Python 2.x
# Constants are usually just string word of itself.
# Oddly, all but tkinter.READABLE and tkinter.WRITABLE are repeated
# in tkinter.constants
# Tk is the root window, Frame is a container
# tkinter.Frame != tkinter.ttk.Frame.  For example ttk has no background attribute
# It is always a bad design choice to have two classes that almost, but not quite, identical

def get_geometry(window):
    """ return window geometry as list of xpos, ypos, xwidth, ywidth """
    geom = window.geometry()
    coord_strings = re.match('(\d+)x(\d+)\+(\d+)\+(\d+)', geom).groups()
    coords= [int(c) for c in coord_strings]
    return coords


def center_window(top, width=290, height=150):
    """ Center top level window in screen

    Might be imperfect, see discussion at
    http://stackoverflow.com/questions/3352918
"""
    top.update_idletasks()
    # update_idle_tasks does geometry packing pending w/o callbacks

    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    width, height, old_x, old_y = get_geometry(top)

    new_x = (screen_width - width) // 2
    new_y = (screen_height - height) // 2
    geom = '{}x{}+{}+{}'.format(width, height, new_x, new_y)
    print("new geometry:", geom)
    top.geometry(geom)


def raise_window(window):
    """ raise window over other application windows.

    http://stackoverflow.com/questions/1892339/make-tkinter-jump-to-the-front
    """
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

def main():
    print("Running")
    root = tk.Tk()
    root["background"] = "red"
    root.title("Press OK when done")
    # setting this to red tends to make a 'flash' of red before the frame inside
    # is rendered, coverting this background.

    frame_above = tk.Frame(root, relief=tk.RAISED, borderwidth=2)
    # a borderwidth of 1 is just a line at the bottom, too small for effect
    frame_above['bg'] = 'yellow'
    frame_above.pack(fill=tk.BOTH, expand=1)
    # pack, which is not frame, will pack the zero widgets together against
    # the top edge, expand to fill the parent (root) in BOTH x and y
    # directions.  Expand the space even if the (nonexistant) widgets in
    # the frame don't need it,

    button_frame = tk.Frame(root)
    button_frame['bg'] = "blue"
    button_frame.pack(fill=tk.X)
    # So, the side is by default top, so this goes under.  The fill means
    # it will take up the entire width, so that the buttons inside can
    # live a particular side of the full width.

    closeButton = tk.Button(button_frame, text="Close",
                            command=button_frame.quit)
    # so the command quit kills all widgets and ends the Tcl/tk
    # interpreter.  Lack of documentation makes is sound the same
    # as destroy.   Could use any frame's quit.
    closeButton.pack(side=tk.RIGHT, padx=5, pady=5)
    # pack, but with a preference towards the middle of right side.
    okButton = tk.Button(button_frame, text="OK")
    okButton.pack(side=tk.RIGHT, padx=5, pady=5)
    # again on the right side, but the far right is taken, so towards the
    # middle more.
    #frame1.pack(fill=tk.BOTH, expand=1)
    # pack geometry manager with expand in both directions

    # Note that printing a window geometry now would give me a 1x1

    #center_window(root)
    raise_window(root)
    print("ready for mainloop")
    root.mainloop()
    # So, final version is going to be just that blue background of the
    # button_frame.  The window will be just high enough and wide enough
    # for the buttons.   Making the window wider will leave buttons on
    # the right edge.  Making the window higher will leave a blue bar
    # along the bottom, and the yellow above_frame along the top.


    print("Ran.")

if __name__ == "__main__":
    main()
