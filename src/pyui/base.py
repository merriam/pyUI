""" pyui Base abstract class.

This defines the interface for subclasses.
"""

from contextlib import contextmanager
from . import except_pyui_usage, Spec
from logging import warning, info, debug

class Base():
    """The pyui gui base abstract class; usable through subclassing.

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
            raise except_pyui_usage("Only instantiate subclasses of Base.")

    def dialog(self, spec_item, current_values=None):
        """   main dialog system.
        self = a subclass of pyui.
        spec_item = mini-language for fields in dialog,
        current_values = dict of current values for fields
        TODO:  should be a class method
        """
        self.previous_values = current_values
        # we prepared for adding items in the __init__() function.
        self.add_item(Spec(spec_item))  # Add whole spec
        if self.conclude():
            return self.values
        else:
            return None

    def add_item_dict(self, spec):  raise NotImplementedError
    def add_item_grid(self, spec):  raise NotImplementedError
    def add_item_entry(self, spec): raise NotImplementedError
    def add_item_label(self, spec): raise NotImplementedError

    def add_item(self, spec):
        """ Add spec to current window or frame.

        Note that this can be recursive in that adding a collection will
        in turn call this routine for each item.
        Yes, this feels like ugly code ripe for inherience. """

        if spec.kind is Spec.Kinds.ENTRY:
            return self.add_item_entry(spec)
        elif spec.kind is Spec.Kinds.LABEL:
            return self.add_item_label(spec)
        elif spec.kind is Spec.Kinds.GRID:
            return self.add_item_grid(spec)
        elif spec.kind is Spec.Kinds.LIST:
            return self.add_item_list(spec)
        elif spec.kind is Spec.Kinds.DICT:
            return self.add_item_dict(spec)
        else:
            raise except_pyui_usage("Odd kind {}".format(spec.kind))

    def conclude(self):
        """ Execute, after dialog adds all fields.  Sets self.values dict
            for the return.  It seems more convenient to have self.values
            than a return value.

            Returns True on ok, or input accpted, and False on cancel or ignore
            the page.  """
        raise NotImplementedError
