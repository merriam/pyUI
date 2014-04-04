""" pyui.echo for echoing back the specification.  Primarily a testing aid.

"""

import pyui
from . import Spec
from nose.tools import raises, eq_
from contextlib import contextmanager
import re
from io import StringIO


class Echo(pyui.Base):
    """a text echo testing class for pyui.

    This class stretches the contract a bit, in that the return value
is just a string with the debug echo of parsing up the spec.  Later,
it may be that plus some default values, depending on the tests that
should be written.

    """
    def __init__(self):
        """ First step """
        super().__init__()
        self.indent = 0
        self.emit_io = StringIO()
        self.values["echo"] = ""

    def emit(self, message):
        """ This is the only output of this class. """
        print("{:2}:{}{}".format(self.indent, ' ' * self.indent, message),
               file=self.emit_io)
        self.values["echo"] = self.emit_io.getvalue()

    @contextmanager
    def section(self, message):
        """ emit the section hearder and footer """
        self.emit(">{}".format(message))
        self.indent += 1
        yield
        self.indent -= 1
        self.emit("<{}".format(message))

    def add_item_dict(self, spec):
        with self.section("Dict with {} keys".format(len(spec.v))):
            keys = spec.value.keys()
            if type(spec.v) is dict:
                keys= sorted(keys)  # sort keys only if a basic dict.
                for key in keys:
                    value = spec.value[key]
                    self.add_item(Spec.new_label(key))
                    self.add_item(Spec(value))

    def add_item_grid(self, spec):
        with self.section("Grid with {} rows and {} columns".format(
                  len(spec.value), len(spec.value[0]))):
            for row_num, row in enumerate(spec.value):
                with self.section("grid row {}".format(row_num)):
                    for col_num, cell in enumerate(row):
                        with self.section("grid item at ({}, {})".format(
                                row_num, col_num)):
                            self.add_item(Spec(cell))

    def add_item_list(self, spec):
        with self.section("List with {} rows".format(len(spec.value))):
            for row_num, row in enumerate(spec.value):
                with self.section("list item {}".format(row_num)):
                    self.add_item(Spec(row))

    def add_item_label(self, spec):
        self.emit("Adding label {}".format(spec.value))

    def add_item_entry(self, spec):
        self.emit("Adding entry {}".format(spec.value))
        self.values[spec.value] = 0  # hack, need to know type.

    def conclude(self):
        """ Execute, after dialog adds all fields.  Sets self.values dict
            for the return.  It seems more convenient to have self.values
            than a return value.

            Returns True on ok, or input accpted, and False on cancel or ignore
            the page.  """
        return True

    def add_entry_spec(self, spec):
        """ Add an input, e.g., a string to fill in.  """
        self.emit("INPUT: {}".format(spec))

    def add_data_spec(self, spec):
        """ Add a data spec, e.g., a label. """
        self.emit("::{}".format(spec))

if __name__ == "__main__":
    except_pyui_usage("You are trying to run the echo module.")
