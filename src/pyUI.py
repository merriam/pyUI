""" PyUI Module for introspection based UI.  See docs. """

def _dialog_stub_numbers(arg):
    print("arg=", arg)
    return {"number1": 5, "number2": 8}

def _dialog_stub_display(arg):
    print("arg=", arg)
    return None

def dialog(arg):
    """ Accept a data type, run a dialog, and return a sample """
    return _dialog_stub_numbers(arg)

if __name__ == "__main__":
    print("You are trying to run the module.")
    print("This should have 'doctor' self-test or demo mode.")
