""" stub.py  Minimalist UI stub for testing.
"""

from . import Base

class Stub(Base):
    """ A stub class for pyUI.  It ignores the spec, and returns
        a constant dictionary.   """
    # pylint: disable=abstract-method,no-init
    def dialog(self, spec=None, current_values=None):
        """ fake dialog and return immediately """
        print(spec)
        if isinstance(spec, str):
            return None
        else:
            return {"number1": 5, "number2" : 8}
