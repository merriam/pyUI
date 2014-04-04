""" Test if all basic imports work. """

from nose.tools import raises, eq_

def test_pass():
    assert True

@raises(AssertionError)
def test_not_fail():
    assert False

def test_import_pyui():
    import pyUI

def test_import_spec():
    import pyUI.spec

def test_import_base():
    import pyUI.base

def test_import_uis():
    import pyUI.stub
    import pyUI.echo
    # import pyUI.text
    import pyUI.tk
    # import pyUI.flask
