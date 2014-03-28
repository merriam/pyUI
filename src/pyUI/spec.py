""" PyUI Module for introspection based UI.

The plan is in docs/plan.md.   Additional comments are in docs/log.md or may the
git commit messages. """

# TODO, add module for what gets exported.


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
