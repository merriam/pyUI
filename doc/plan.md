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

So, in a bit more depth, I'm looking at design with these major terms:

Spec: The description of what items of data are wanted.  The spec is
recursives, in that a data item might be iteself a list of items.
This implies an iterator that may return new spec objects.  The spec
is also might have lists of lists of dicts of lists.  Determining the
data items requested from a raw spec is a puzzle: there might be
english phrases; sample values; or other hints.  Treating it like a
puzzle burdens the ui system programmer instead of the client.  In a
perfect implementation, any call to the library that could be figured
out by a human should work.

BaseUI: The abstract base UI of the system on which specific
subclasses will implement the display for HTML, Tcl/Tk, or other systems.   It should have then contract that each subclass must implement.

Other files are experiments, examples, and docs.
