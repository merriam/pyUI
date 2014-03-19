Plan for PyUI
--

This is an itch I've been wanting to scratch for a while.   I want a introspection based GUI.

In the simplest form, I'll have a non-blocking dialog type gui:

     import pyUI as ui
     fields = [["Enter first number:", "{[number1]:d}"],
               ["Enter second number", "{[number2]:d}"]]
     output = ui.dialog(fields)
     total = output["number1"] + output["number2"]
     output = ui.dialog("Total value is {}".format(total))


There is enough information here to do a simple Tcl/TK system.  I'm using the mini-language
for format for specifying the inputs.

)
