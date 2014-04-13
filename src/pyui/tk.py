""" tk.py tk subclass for tcl/tk ui.
    python3, of course.
"""

from nose.tools import raises, eq_
from contextlib import contextmanager
import re
from . import except_pyui, except_pyui_usage, Base, debug, spec
import tkinter as tk
import tkinter.constants as c
import tkinter.ttk as ttk
# note that tk and ttk share many names
from .spec import parse_entry_spec

# Some handy tk utilities
def get_geometry(window):
    """ return window geometry as list of xpos, ypos, xwidth, ywidth """
    top.update_idletasks()
    # update_idle_tasks does geometry packing pending w/o callbacks
    # failure to call this means that geometry() tends to return a
    # a size of 1x1.   Why window.geometry() doesn't just call it is one
    # of those broken software things.
    geom = window.geometry()
    coord_strings = re.match('(\d+)x(\d+)\+(\d+)\+(\d+)', geom).groups()
    coords= [int(c) for c in coord_strings]
    return coords


def center_window(top):
    """ Center top level window in screen

    Might be imperfect, see discussion at
    http://stackoverflow.com/questions/3352918
"""
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

###


class Tk(Base):
    """ The specific pyui for tk.

    Ah, the curse of inheritence.  I think it actually the
    right choice here.  """

    # pylint: disable=super-on-old-class
    # pylint is buggy
    def __init__(self):
        """ Prepare tableau, once before a dialog
            root (windowing system) has
               top_frame (where content goes) and
               bottom_frame (where buttons go)
        """
        super().__init__()
        self.root = tk.Tk()  # different Tk than this class.
        self.root.title("Python Pyui!")

        self.top_frame = tk.Frame(self.root, bg="yellow")
        self.top_frame.pack(fill=tk.BOTH, expand=1)
        self.bottom_frame = tk.Frame(self.root, bg="blue",
                                     borderwidth=1, relief=tk.RAISED)
        okButton = tk.Button(self.bottom_frame, text="OK",
                             command=self.cb_ok)
        okButton.pack(fill='none', expand=1, side=c.RIGHT)
        cancelButton = tk.Button(self.bottom_frame, text="Cancel",
                                  command=self.cb_cancel)
        cancelButton.pack(fill='none', expand=1, side=c.RIGHT)
        self.ok_return = True  # ???

    def conclude(self):
        """Execute main loop of system and prepare self.values.

        This should be done after init and adding fields, of course.
        """
        center_main_window(self.root)
        raise_window(self.root)
        self.root.mainloop()
        debug("TK concluded.")
        return self.ok_return

    def dialog(self, spec):
        pass

    def cb_ok(self):
        """on OK button, copy into self.values hash.

        Note that no known callback triggered on field
        triggered when cursor is in the field, and then OK is
        pressed.
        """
        debug("in ok")
        self.values = None # ??? fix me
        self.ok_return = True
        self.root.quit()  # end mainloop

    def cb_cancel(self):
        """ cancel button """
        debug("in cancel")
        self.values = None
        self.ok_return = False
        self.root.quit()  # end mainloop

    def add_item_dict(self, the_spec): pass
    def add_item_grid(self, the_spec): pass
    def add_item_list(self, the_spec): pass
    def add_item_label(self, the_spec): pass
    def add_item_entry(self, the_spec):
        """ Add an input entry, e.g., a string to fill in.  """
        debug("Adding entry {}".format(Spec))
        return
        """
        parse = parse_entry_spec(the_spec)
        name = parse["name"]
        var = tkinter.IntVar()
        entry = ttk.Entry(textvariable=var)

        if self.previous_values and name in self.previous_values:
            var.set(self.previous_values[name])
        entry.bind("<Enter>", self.cb_copy_coupled_values)
        entry.pack()
        self.coupled_entries[name] = var
        """

    def add_data_spec(self, the_spec):
        """ Add a data spec, e.g., a label. """
        return
        """
        a_label = ttk.Label(self.frame, text=spec)
        a_label.pack(fill=c.BOTH, expand=1)
        # self.emit("::{}".format(spec))
        """

if __name__ == "__main__":
    except_pyui_usage("You are trying to run the module.")
