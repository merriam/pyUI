[![Build Status](https://travis-ci.org/merriam/pyui.svg?branch=master)](https://travis-ci.org/merriam/pyui)

Plan for PyUI
--

This is an itch I've been wanting to scratch for a while.  I want a different UI.  This should have major innovations in the
following areas:

* same or near same interface to Tck/Tk, Terminal, HTML, MS-Windows, OS/X,
  Ipad, iPhone, and Android.  Maybe even Glade, wxWindows, and Qt.
* availability of non-blocking UI items, meaning a dialog where the event
  loop doesn't take over the applicaiton.  Call to get values and have it
  return.
* Lazy specification with smart layouts.  I should be able to toss over raw
  data, english phrases to parse, or raw data and get something reasonable.
* Smart data types, not just 'int' but 'year' or 'counting number' or
  'modern year' or something.  Also, SSN, real addresses, phone numbers,
  zip codes, etc.
* A general tone of kicking all possible work to the library instead of the
  developer.  Treating the input as a puzzle that could be worked out by
  the library cuts down on the client's need to puzzle out a specific
  interface.

In the simplest form, I'll have a non-blocking dialog type gui:

     import pyUI as ui
     fields = [["Enter first number:", ":number1 is integer"],
               ["Enter second number", ":number2 is integer"]]
     output = ui.dialog(fields)
     total = output["number1"] + output["number2"]
     output = ui.dialog("Total value is {}".format(total))


There is enough information here to do a simple Tcl/TK system, so it should be enough for the library to run.

To understand in a bit more depth, read the [Glossary](DEVELOP.md) and other sections of [the development guide](DEVELOP.md).
