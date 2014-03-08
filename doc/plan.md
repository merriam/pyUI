Plan for PyUI
--

This is an itch I've been wanting to scratch for a while.   I want a introspection based GUI.

In the simplest form, I'll have a non-blocking dialog type gui:

     import pyUI
     fields = [ ["Enter first number:", "{int number1}"], ["Enter second number", "{int number2}"] ]
     output = pyUI.dialog(fields)
     total = output["number1"] + output["number2"]
     output = pyUI.dialog("Total value is " + total)

There is enough information here to do a simple Tcl/TK system.
