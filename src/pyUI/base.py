""" pyUI Base abstract class.

This defines the interface for subclasses.
"""

from contextlib import contextmanager
from . import except_pyUI_usage
from .spec import is_grid, is_entry_spec

class Base():
    """The pyUI gui base abstract class; usable through subclassing.

    Its was a tough call to decide subclassing was the correct choice.
    The trade-off of being able over-ride dialog() tipped the scales
    away from having a different class implement an interface.

    TODO: new contract The base class keeps the contract for all GUIs.

    So, far, all UIs seem to have a workflow of a.  initialize system,
    b.  add widgets, c.  run the mainloop, d.  return the values.  e..
    shutdown the ui.

    """

    def __init__(self):
        """ This is called as a UI is instantiated.   For subclasses,
        this is also a 'prepare' module, doing any operations necessary
        before the first call is made.

        """
        self.values = {}
        self.previous_values = None
        if type(self) == Base:
            raise except_pyUI_usage("Only instantiate subclasses of Base.")

    def dialog(self, spec, current_values=None):
        """   main dialog system.
        self = a subclass of pyUI.
        spec = mini-language for fields in dialog,
        current_values = dict of current values for fields
        TODO:  should be a class method
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

        TODO:  rewrite
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
