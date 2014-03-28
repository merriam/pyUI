"""  __init.py__, run whenever this module is imported.

This also dictates what code should be at the top level
of the module.   I'm taking the approach that it allows
me to scaffold out the library, then fix up the divisions
among files later.
"""

#-- Module exceptions
class except_pyUI(BaseException):
    """ Superclass for all custom exceptions from this library """
    pass

class except_pyUI_usage(except_pyUI):
    """ When a programmer has called the library incorrectly. """
    pass

from .base import Base
from .tk import Tk
from .stub import Stub
Echo = Stub
HTML = Stub
