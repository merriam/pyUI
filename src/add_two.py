""" Simple integration test to add two numbers using several specific gui systems """

import pyUI

def add_two(ui):
    """ Add two using the pyUI subclass given. Returns total.  """
    fields = [["Enter first number:", ":number1 is number"],
              ["Enter second number", ":number2 is number"]]
    output = ui().dialog(fields)
    if output:
        total = output["number1"] + output["number2"]
        output = ui().dialog("Total value is {}".format(total))
        return total
    return None

if __name__ == "__main__":
    print("==== Next up:  Stub ===")
    add_two(pyUI.Stub)
    print("==== Next up:  Echo ====")
    add_two(pyUI.Echo)
    #print("==== Next up:  Tk ====")
    #add_two(pyUI.tk)
    #print("==== Next up:  Flask ====")
    #add_two(pyUI.flask)

#from pyUI import FIELD, DATA, f, d
#fields = [[DATA+"Enter first number:", FIELD+"number1 is number"]]
#fields = [d("Enter first number:"), f("number1 is int)]
#fields = [[d(":Boom:"), f("number is like '999' with read background"]]
#fields = ":a_string"
