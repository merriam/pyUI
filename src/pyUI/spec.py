""" PyUI Module for introspection based UI.

The plan is in docs/plan.md.   Additional comments are in docs/log.md or may the
git commit messages. """

# TODO, add module for what gets exported.

from tkinter import Tk, BOTH, RIGHT, LEFT, RAISED, Label
import tkinter
from tkinter.ttk import Frame, Button, Style, Entry
from nose.tools import raises, eq_
from contextlib import contextmanager
import re

class except_pyUI(BaseException):
    pass

class except_pyUI_usage(except_pyUI):
    pass

#====== Spec stuff
# an Entry_spec, which may be a class later, is the minilanguage describing an entry.
# For example, ":number" or ":number like 999".
# Note that parsing it also requires looking at a current value:  we might infer a type.

PREFIX = ":"

def is_entry_spec(spec):
    """ check if current spec is an entry_spec """
    assert isinstance(spec, str)
    return len(spec) > 1 and spec[0] == PREFIX and spec[1] != PREFIX

def test_is_entry():
    assert is_entry_spec(":number")
    assert is_entry_spec(":number is like '999'")
    assert not is_entry_spec("Number")
    assert not is_entry_spec(":")
    assert not is_entry_spec("::data")
    assert not is_entry_spec("A label")
    assert not is_entry_spec("foo:")

def parse_entry_spec(entry_spec):
    """ parse entry spec into dictionary of information """
    assert is_entry_spec(entry_spec)
    parse = {}
    words = entry_spec[1:].split()
    parse["name"] = words[0]
    return parse

def test_parse_entry_spec():
    # TODO:  Check for more than name
    assert parse_entry_spec(":number")["name"] == "number"
    assert parse_entry_spec(":number like '999'")["name"] == "number"


def is_grid(spec):
    """ return True for list of (lists of same length) """
    if isinstance(spec, list) and isinstance(spec[0], list):
        target_length = len(spec[0])
        for item in spec[1:]:
            if not isinstance(item, list) or len(item) != target_length:
                return False
        return True
    return False

def test_is_grid():
    assert is_grid([[]])
    assert is_grid([[1], [2]])
    assert is_grid([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
    assert not is_grid(2)
    assert not is_grid({'a':'b'})
    assert not is_grid(['s'])
    assert not is_grid([[1], [2, 3], [4]])

def is_simple(spec):
    """ return True for non-list, non-dicts """
    return not (isinstance(spec, list) or isinstance(spec, dict))

def test_is_simple():
    assert is_simple('label')
    assert is_simple(3.4)
    assert is_simple(None)
    assert not is_simple([])
    assert not is_simple({})


#def raise_above_all(window):
#    # doesn't work
#    window.xattributes('-topmost', 1)
#    window.attributes('-topmost', 0)

#===========  pyUI
WINDOWING_SYSTEMS = ["tk", "text", "stub"]

class Base(object):
    """The pyUI gui base abstract class.  Not directly usable: a subclass
    must add the ui specific methods for preparing (during __init__),
    concluding, and adding all the values.

    Its was a tough call to decide subclassing was the correct choice.  The
    trade-off of being able over-ride dialog() tipped the scales away from
    having a different class implement an interface.

    """

    def __init__(self):
        """ This is called as a UI is instantiated.   For subclasses,
        this is also a 'prepare' module, doing any operations necessary
        before the first call is made.

        Every subclass must declare an __init__ method and then call this as
        part of the init.
        """
        self.values = {}
        self.previous_values = None
        if type(self) == pyUI:
            raise except_pyUI_usage("Only instantiate base PyUI subclasses.")

    def dialog(self, spec, current_values=None):
        """   main dialog system.
        self = a subclass of pyUI.
        spec = mini-language for fields in dialog,
        current_values = dict of current values for fields
        """
        self.previous_values = current_values
        # we prepared for adding items in the __init__() function.
        self.add_spec(spec)  # Add whole spec
        if self.conclude():
            return self.values
        else:
            return None


    def add_spec(self, spec):
        """ Add spec to current window or frame.

        Not that this is recursive, so a dict that contains a list value
        would recurse as it writes that list value.

        Another design trade-off:  this is a long function so that
        it recurses only from itself.
        """
        if isinstance(spec, list):
            if is_grid(spec):
                with self.grid_spec(spec):
                    for row in spec:
                        with self.grid_row(row):
                            for col in row:
                                with self.grid_item(col):
                                    self.add_spec(col)
            else:   # other list
                with self.list_spec(spec):
                    for item in spec:
                        with self.list_item(item):
                            self.add_spec(item)
        elif isinstance(spec, dict):
            with self.dict_spec(spec):
                for key in sorted(spec.keys()):
                    value = spec[key]
                    with self.dict_key_value(key, value):
                        self.add_spec(key)
                        with self.dict_value(value):
                            self.add_spec(value)
        elif is_entry_spec(spec):
            self.add_entry_spec(spec)
        else:
            self.add_data_spec(spec)  # determine acceptable types?

    # Declare implementations of these methods in subclasses
    # Also declare a __init__()

    def conclude(self):
        """ Execute, after dialog adds all fields.  Sets self.values dict
            for the return.  It seems more convenient to have self.values
            than a return value.

            Returns True on ok, or input accpted, and False on cancel or ignore
            the page.  """
        raise NotImplementedError

    def add_entry_spec(self, spec):
        """ Add an input, e.g., a string to fill in.  """
        raise NotImplementedError

    def add_data_spec(self, spec):
        """ Add a data spec, e.g., a label. """
        raise NotImplementedError

    @contextmanager
    def grid_spec(self, spec):
        """ Context manager when adding an entire grid. """
        raise NotImplementedError

    @contextmanager
    def grid_row(self, spec):
        """ Context manager when adding a row to a grid. """
        raise NotImplementedError

    @contextmanager
    def grid_item(self, spec):
        """ Context manager when adding an item to a grid,
            meaning one cell of one row. """
        raise NotImplementedError

    @contextmanager
    def list_spec(self, spec):
        """ Context manager when adding a list . """
        raise NotImplementedError

    @contextmanager
    def list_item(self, spec):
        """ Context manager when adding a single item on a list. """
        raise NotImplementedError

    @contextmanager
    def dict_spec(self, spec):
        """ Context manager when adding a dict. """
        raise NotImplementedError

    @contextmanager
    def dict_key_value(self, key, value):
        """ Context manager when adding a key, value pair to a dict. """
        raise NotImplementedError

    @contextmanager
    def dict_value(self, value):
        """ Context manager when adding just the dict_value. """
        raise NotImplementedError

@raises(except_pyUI)
def test_dialog():
    pyUI().dialog("asdf")

@raises(except_pyUI_usage)
def test_dialog_2():
    pyUI().dialog("asdf")


#======== pyUI_stub
class Stub(Base):
    """ A stub class for pyUI """
     # pylint: disable=abstract-method
    def dialog(self, spec, current_values=None):
        print(spec)
        if isinstance(spec, str):
            return None
        else:
            return {"number1": 5, "number2" : 8}
#=== tk stuff
def get_centering_geometry(width, height, screen_width, screen_height):
    """ return geometry string for given window and screen size """
    new_x = (screen_width - width) // 2
    new_y = (screen_height - height) // 2
    return '{}x{}+{}+{}'.format(width, height, new_x, new_y)

def test_get_centering_geometry():
    eq_(get_centering_geometry(100, 100, 400, 400), "100x100+150+150")
    eq_(get_centering_geometry(100, 200, 300, 400), "100x200+100+100")


 #====== pyUI_tk
class pyUI_tk(Base):
    """ The specific pyUI for tk.  TODO:  make this pyUI.tk

     I will heed the advie of http://effbot.org/tkinterbook/grid.htm
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

    def __init__(self):
        """ Prepare, once befoer a dialog
            root (windowing system) has
               main (visible window space) has
                   frame (place with all the fields) and
                   some butons """
        super().__init__()
        print("Running")
        self.root = Tk()
        self.main = Frame(self.root)
        self.main.parent = self.root
        self.root.title("Python!")
        self.main.style = Style()
        self.main.style.theme_use("default")
        # themes should be 'clam', 'alt', 'classic', and 'default' but
        # I haven't seen a change between these styles.
        self.frame = Frame(self.root, relief=RAISED, borderwidth=1)
        self.coupled_entries = {}
        # see python.org/3.0/library/tkinter.html#coupling-widget-variables
        self.ok_return = True

    def conclude(self):
        """ After addint the fields, this add cancel and OK buttons, Execute main loop of
        system and prepare self.values. """
        self.frame.pack(fill=BOTH, expand=1)
        okButton = Button(self.main, text="OK", command=self.cb_ok)
        cancelButton = Button(self.main, text="Cancel", command=self.cb_cancel)
        okButton.pack(fill='none', expand=1, side=RIGHT)
        cancelButton.pack(fill='none', expand=1, side=RIGHT)
        self.main.pack(fill=BOTH, expand=1)
        self.center_main_window()
        self.root.mainloop()
        print("Ran.")
        return self.ok_return

    def cb_copy_coupled_values(self, tk_event):
        """ Callback to copy from vars coupled to widgets to pkUI
        super class .values for return. """
        for name, coupled_value in self.coupled_entries.items():
             try:
                 value = coupled_value.get()
                 self.values[name] = value
                 print("name ", name, "coupled to", coupled_value, "=", value)
             except ValueError:
                 pass  # couldn't convert to int or other value

    def cb_ok(self):
        """ on OK button.
        Note that no known callback triggered on field triggered when cursor is in the field,
        and then OK is pressed. """
        print("in ok")
        self.cb_copy_coupled_values(None)
        self.ok_return = True
        self.main.quit()

    def cb_cancel(self):
        print("in cancel")
        self.values = None
        self.ok_return = False
        self.main.quit()

    def add_entry_spec(self, entry_spec):
        """ Add an input entry, e.g., a string to fill in.  """
        parse = parse_entry_spec(entry_spec)
        name =  parse["name"]
        var = tkinter.IntVar()
        entry = Entry(textvariable=var)

        if self.previous_values and name in self.previous_values:
            var.set(self.previous_values[name])
        entry.bind("<Enter>", self.cb_copy_coupled_values)
        entry.pack()
        self.coupled_entries[name] = var

    def add_data_spec(self, spec):
        """ Add a data spec, e.g., a label. """
        a_label = Label(self.frame, text=spec)
        a_label.pack(fill=BOTH, expand=1)
        # self.emit("::{}".format(spec))

    @contextmanager
    def grid_spec(self, spec):
        """ Context manager when adding an entire grid.

         """
        # First, add a frame, because mixing grids directly causes
        # all sorts of problems for tk layout managers.
        new_frame = Frame(self.frame)
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


#===== More unit tests

def check_valid_pyUI_object(obj):
    """ make sure object has overriddent required virual methods. """
    assert isinstance(obj, Base)
    required = ['__init__', 'conclude', 'grid_spec',
                'grid_row', 'grid_item', 'list_spec', 'list_item',
                'dict_spec', 'dict_key_value', 'dict_value',
                'add_entry_spec', 'add_data_spec']
    for method in required:
        assert hasattr(Base, method), "pyUI should have {}".format(method)
        assert hasattr(obj, method)
        assert callable(getattr(obj, method))
        assert getattr(pyUI, method) != getattr(type(obj), method), \
                "Subclass missing virtual method: {}".format(method)

def test_pyUI_tk_complete():
    check_valid_pyUI_object(pyUI_tk())

if __name__ == "__main__":
    except_pyUI_usage("You are trying to run the module.")
