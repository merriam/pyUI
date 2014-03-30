""" tk.py tk subclass for tcl/tk ui.
"""

from nose.tools import raises, eq_
from contextlib import contextmanager
import re
from . import except_pyUI, except_pyUI_usage, Base
import tkinter
import tkinter.constants as c
import tkinter.ttk as ttk
from .spec import parse_entry_spec

def get_centering_geometry(width, height, screen_width, screen_height):
    """ return geometry string for given window and screen size """
    new_x = (screen_width - width) // 2
    new_y = (screen_height - height) // 2
    return '{}x{}+{}+{}'.format(width, height, new_x, new_y)

def test_get_centering_geometry():
    eq_(get_centering_geometry(100, 100, 400, 400), "100x100+150+150")
    eq_(get_centering_geometry(100, 200, 300, 400), "100x200+100+100")

class Tk(Base):
    """ The specific pyUI for tk.

     I will heed the advice of http://effbot.org/tkinterbook/grid.htm
     and remove all pack commands. """

    def center_main_window(self, width=990, height=150):
        """ center parent window in screen.

        Might only work after packing the window, unclear. """
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(get_centering_geometry(width, height,
                            screen_width, screen_height))

    # pylint: disable=super-on-old-class
    # pylint is buggy
    def __init__(self):
        """ Prepare, once befoer a dialog
            root (windowing system) has
               main (visible window space) has
                   frame (place with all the fields) and
                   some butons """
        super().__init__()
        print("Init of TK")
        self.root = tkinter.Tk()  # not the name of this class.
        self.main = ttk.Frame(self.root)
        self.main.parent = self.root
        self.root.title("Python!")
        self.main.style = ttk.Style()
        self.main.style.theme_use("default")
        # themes should be 'clam', 'alt', 'classic', and 'default' but
        # I haven't seen a change between these styles.
        self.frame = ttk.Frame(self.root, relief=c.RAISED, borderwidth=1)
        self.coupled_entries = {}
        # see python.org/3.0/library/tkinter.html#coupling-widget-variables
        self.ok_return = True

    def conclude(self):
        """After adding the fields, this add cancel and OK buttons, Execute
        main loop of system and prepare self.values.
        """
        self.frame.pack(fill=c.BOTH, expand=1)
        okButton = ttk.Button(self.main, text="OK", command=self.cb_ok)
        cancelButton = ttk.Button(self.main, text="Cancel",
                                  command=self.cb_cancel)
        okButton.pack(fill='none', expand=1, side=c.RIGHT)
        cancelButton.pack(fill='none', expand=1, side=c.RIGHT)
        self.main.pack(fill=c.BOTH, expand=1)
        self.center_main_window()
        self.root.mainloop()
        print("TK conclude concluede.")
        return self.ok_return

    def dialog(self, values, spec_hints):
        pass

    def cb_copy_coupled_values(self, tk_event):
        """ Callback to copy from vars coupled to widgets to pkUI
        super class .values for return. """
        for name, coupled_value in self.coupled_entries.items():
            try:
                value = coupled_value.get()
                self.values[name] = value
                print("name ", name, "coupled to", coupled_value,
                      "=", value)
            except ValueError:
                pass  # couldn't convert to int or other value

    def cb_ok(self):
        """on OK button.

        Note that no known callback triggered on field
        triggered when cursor is in the field, and then OK is
        pressed.
        """
        print("in ok")
        self.cb_copy_coupled_values(None)
        self.ok_return = True
        self.main.quit()

    def cb_cancel(self):
        """ cancel button """
        print("in cancel")
        self.values = None
        self.ok_return = False
        self.main.quit()

    def add_entry_spec(self, entry_spec):
        """ Add an input entry, e.g., a string to fill in.  """
        parse = parse_entry_spec(entry_spec)
        name = parse["name"]
        var = tkinter.IntVar()
        entry = ttk.Entry(textvariable=var)

        if self.previous_values and name in self.previous_values:
            var.set(self.previous_values[name])
        entry.bind("<Enter>", self.cb_copy_coupled_values)
        entry.pack()
        self.coupled_entries[name] = var

    def add_data_spec(self, spec):
        """ Add a data spec, e.g., a label. """
        a_label = ttk.Label(self.frame, text=spec)
        a_label.pack(fill=c.BOTH, expand=1)
        # self.emit("::{}".format(spec))

    '''
    @contextmanager
    def grid_spec(self, spec):
        """ Context manager when adding an entire grid.

         """
        # First, add a frame, because mixing grids directly causes
        # all sorts of problems for tk layout managers.
        new_frame = ttk.Frame(self.frame)
        # It's a class, so I'm going to dump data I want isolated on the stack here.
        new_frame._next_row = 0
        new_frame._next_col = 0
        new_grid = Grid()
        saved_frame = self.frame
        self.frame = new_frame
        yield
        self.frame = saved_frame

    @contextmanager
    def grid_row(self, spec):
        """ Context manager when adding a row to a grid. """
        # self.section_start("Grid row")
        yield
        # self.section_end("Grid row")

    @contextmanager
    def grid_item(self, spec):
        """ Context manager when adding an item to a grid,
            meaning one cell of one row. """
        # self.section_start("Grid item")
        yield
        # self.section_end("Grid item")
    '''



    @contextmanager
    def list_spec(self, spec):
        """ Context manager when adding a list . """
        # self.section_start("List spec")
        yield
        # self.section_end("List spec")

    @contextmanager
    def list_item(self, spec):
        """ Context manager when adding a single item on a list. """
        # self.section_start("List item")
        yield
        # self.section_end("List item")

    @contextmanager
    def dict_spec(self, spec):
        """ Context manager when adding a dict. """
        # self.section_start("dict spec")
        yield
        # self.section_end("dict spec")

    @contextmanager
    def dict_key_value(self, key, value):
        """ Context manager when adding a key, value pair to a dict. """
        # self.section_start("key value")
        yield
        # self.section_end("key value")

    @contextmanager
    def dict_value(self, value):
        """ Context manager when adding just the dict_value. """
        # self.section_start("value")
        yield
        # self.section_end("value")

if __name__ == "__main__":
    except_pyUI_usage("You are trying to run the module.")
