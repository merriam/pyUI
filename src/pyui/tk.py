""" tk.py tk subclass for tcl/tk ui.
    python3, of course.
"""

from nose.tools import raises, eq_
from contextlib import contextmanager
import re
from . import except_pyui, except_pyui_usage, Base, debug, Spec
import tkinter as tk
import tkinter.constants as c
import tkinter.ttk as ttk
# note that tk and ttk share many names
from .spec import parse_entry_spec

# Some handy tk utilities
def get_geometry(window):
    """ return window geometry as list of xpos, ypos, xwidth, ywidth """
    window.update_idletasks()
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
    right choice here.

    Tk is a bit odd.  Inside a grid, I cannot pack.   Outside
    a grid, I must pack.  Each item must know its current parent.
    All sorts of messes.
"""

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
        self.top_frame.pack(fill=c.BOTH, expand=1)
        self.bottom_frame = tk.Frame(self.root, bg="blue",
                                     borderwidth=1, relief=c.RAISED)
        self.bottom_frame.pack(fill=c.X)
        okButton = tk.Button(self.bottom_frame, text="OK",
                             command=self.cb_ok)
        okButton.pack(fill='none', padx=5, pady=5, side=c.RIGHT)
        cancelButton = tk.Button(self.bottom_frame, text="Cancel",
                                  command=self.cb_cancel)
        cancelButton.pack(fill='none', padx=5, pady=5, side=c.RIGHT)

        self.not_cancelled = False
        self.current_parent = self.top_frame
        self.parent_is_grid= False
        self.entries = {}

    def conclude(self):
        """Execute main loop of system and prepare self.values.

        This should be done after init and adding fields, of course.
        """
        raise_window(self.root)
        center_window(self.root)
        self.root.mainloop()
        debug("TK concluded.")
        return self.not_cancelled

    def cb_ok(self):
        """on OK button, copy into self.values hash.

        Note that no known callback triggered on field
        triggered when cursor is in the field, and then OK is
        pressed.
        """
        debug("in ok")
        self.values = {}
        for entry_name, entry in self.entries.items():
            self.values[entry_name] = int(entry.get())
        self.not_cancelled = True
        self.root.quit()  # end mainloop

    def cb_cancel(self):
        """ cancel button """
        debug("in cancel")
        self.values = None
        self.not_cancelled = False
        self.root.quit()  # end mainloop

    def add_item_dict(self, the_spec): pass

    def add_item_grid(self, the_spec):
        debug("Adding grid {}".format(the_spec))
        old_parent = self.current_parent
        old_parent_is_grid= self.parent_is_grid

        content_frame = tk.Frame(old_parent, bg="purple")
        self.current_parent = content_frame
        self.current_parent.pack()
        self.parent_is_grid = True

        size= len(the_spec.value)
        for row in range(size):
            for col in range(size):
                cell = the_spec.value[row][col]
                cell_spec = Spec(cell)
                widget = self.add_item(cell_spec)
                widget.grid(row=row, column=col)
        self.current_parent = old_parent
        self.parent_is_grid = old_parent_is_grid
        return content_frame


    def add_item_list(self, the_spec): pass

    def add_item_label(self, the_spec):
        label = tk.Label(self.current_parent, text = the_spec.value)
        if not self.parent_is_grid:
            label.pack()
        return label

    def add_item_entry(self, the_spec):
        """ Add an input entry, e.g., a string to fill in.  """
        debug("Adding entry {}".format(the_spec))
        entry = tk.Entry(self.current_parent)
        self.entries[the_spec.value] = entry
        if not self.parent_is_grid:
            entry.pack()
        return entry

if __name__ == "__main__":
    except_pyui_usage("You are trying to run the module.")
