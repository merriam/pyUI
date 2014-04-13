""" spec, for converting strings into Spec objects.

For example, ":number" or ":number like 999".
Note that parsing it also requires looking at a current value:  we might infer a type.
"""

from nose.tools import raises, eq_
from enum import Enum
from . import except_pyui_usage

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
    eq_(parse_entry_spec(":number")["name"], "number")
    eq_(parse_entry_spec(":number like '999'")["name"],  "number")


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
    assert not is_simple([2,3,4])

class Spec():
    Kinds = Enum("Kinds", "LABEL ENTRY DICT GRID LIST")

    def __init__(self, spec_thing):
        """ Create a spec item from whatever is passed to us. """
        self.value = spec_thing
        self.kind = None
        if is_grid(spec_thing):
            self.kind = self.Kinds.GRID
        elif isinstance(spec_thing, list):
            self.kind = self.Kinds.LIST
        elif isinstance(spec_thing, dict):
            self.kind = self.Kinds.DICT
        elif type(spec_thing) is str and is_entry_spec(spec_thing):
            self.kind = self.Kinds.ENTRY
            parse = parse_entry_spec(spec_thing)
            self.value = parse['name']
        elif type(spec_thing) is str:
            self.kind = self.Kinds.LABEL
        else:
            raise except_pyui_usage("Invalid type: {}".format(type(spec_thing)))

    def __str__(self):
        return "Spec kind:{}  value:{}".format(self.kind, self.value)

    @classmethod
    def new_label(cls, label):
        """ Create a new label spec item from the passed string. """
        return cls.__init__(label)

def test_spec_simples():
   spec = Spec("Enter first number:")
   eq_(spec.value, "Enter first number:")
   eq_(spec.kind, Spec.Kinds.LABEL)

   spec = Spec(":number1")
   eq_(spec.value, "number1")
   eq_(spec.kind, Spec.Kinds.ENTRY)

   spec = Spec(":number1 is an int from 0 to 10")
   eq_(spec.value, "number1")
   eq_(spec.kind, Spec.Kinds.ENTRY)

@raises(except_pyui_usage)
def test_spec_number():
    Spec(3)

def test_spec_collections():
    spec = Spec([1, 2, "buckle my shoe"])
    eq_(spec.value, [1, 2, "buckle my shoe"])
    eq_(spec.kind, Spec.Kinds.LIST)

    g = [ [ 'a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'] ]
    spec = Spec(g)
    eq_(spec.value, g)
    eq_(spec.kind, Spec.Kinds.GRID)

    h = { "hash": 1, "is": 2, "for": 5, "eggs": 'foobar' }
    spec = Spec(h)
    eq_(spec.value, h)
    eq_(spec.kind, Spec.Kinds.DICT)
