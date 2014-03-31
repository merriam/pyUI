""" pyui.echo for echoing back the specification.  Primarily a testing aid.

The plan is in docs/plan.md.   Additional comments are in docs/log.md or may the
git commit messages. """

import pyui
from nose.tools import raises, eq_
from contextlib import contextmanager
import re


class Echo(pyui.Base):
    """ a text echo testing class for pyui """

    def __init__(self):
        """ First step """
        super().__init__()
        self.indent = 0
        self.section_start("pyui_echo:  Preparing")

    def emit(self, message):
        print("{}{}".format(' ' * self.indent, message))

    def section_start(self, message):
        self.emit(">{}".format(message))
        self.indent += 1

    def section_end(self, message):
        self.indent -= 1
        self.emit("<{}".format(message))

    def conclude(self):
        """ Execute, after dialog adds all fields.  Sets self.values dict
            for the return.  It seems more convenient to have self.values
            than a return value.

            Returns True on ok, or input accpted, and False on cancel or ignore
            the page.  """
        self.section_end("pyui_echo:  Concluding")
        return True

    def add_entry_spec(self, spec):
        """ Add an input, e.g., a string to fill in.  """
        self.emit("INPUT: {}".format(spec))

    def add_data_spec(self, spec):
        """ Add a data spec, e.g., a label. """
        self.emit("::{}".format(spec))

    @contextmanager
    def grid_spec(self, spec):
        """ Context manager when adding an entire grid. """
        self.section_start("Grid spec")
        yield
        self.section_end("Grid spec")

    @contextmanager
    def grid_row(self, spec):
        """ Context manager when adding a row to a grid. """
        self.section_start("Grid row")
        yield
        self.section_end("Grid row")

    @contextmanager
    def grid_item(self, spec):
        """ Context manager when adding an item to a grid,
            meaning one cell of one row. """
        self.section_start("Grid item")
        yield
        self.section_end("Grid item")

    @contextmanager
    def list_spec(self, spec):
        """ Context manager when adding a list . """
        self.section_start("List spec")
        yield
        self.section_end("List spec")

    @contextmanager
    def list_item(self, spec):
        """ Context manager when adding a single item on a list. """
        self.section_start("List item")
        yield
        self.section_end("List item")

    @contextmanager
    def dict_spec(self, spec):
        """ Context manager when adding a dict. """
        self.section_start("dict spec")
        yield
        self.section_end("dict spec")

    @contextmanager
    def dict_key_value(self, key, value):
        """ Context manager when adding a key, value pair to a dict. """
        self.section_start("key value")
        yield
        self.section_end("key value")

    @contextmanager
    def dict_value(self, value):
        """ Context manager when adding just the dict_value. """
        self.section_start("value")
        yield
        self.section_end("value")

if __name__ == "__main__":
    except_pyui_usage("You are trying to run the echo module.")
