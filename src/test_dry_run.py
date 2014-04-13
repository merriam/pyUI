""" Integration test that tries to init and add fields """

import pyui

if __name__ == "main":
    t = pyui.Tk()
    grid_fields = [["Enter first number:", ":number1 is number"],
                   ["Enter second number", ":number2 is number"]]
    t.add_item(grid_fields)
