# http://www.tkdocs.com/tutorial/grid.html

from tkinter import *
from tkinter import ttk

#  root
#    content (ttk.Frame) uses grid -- nonresizing whole thing.
#       one, two, three
#       ok, cancel
#       namelbl, name
#       frame (ttk.Frame) -- sunken border part.
root = Tk()

# Adding syle affects if it displays!
#style = ttk.Style().configure('My.TFrame', background=red)
content = ttk.Frame(root)



frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

hello = ttk.Label(frame, text= "Hello")
hello.grid(column=1, row=1)
ttk.Label(frame, text="Goodbye").grid(column=2, row=2)
root.mainloop()
