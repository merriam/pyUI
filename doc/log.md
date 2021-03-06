Monday, April 14, 2014
=============

It's time to look at design a bit more.  I've been kludging together
the Tcl/Tk interface and just starting on the radically different HTML
one.  I'm not trying for good code; I'm trying for code that will
teach me the problem space most completely.  For example, the Base
superclass/Tk subclass split isn't right, but I can't be sure what is
right until I finish the HTML look.

It's odd that I look at the March 19 checklist and find that I did
break out packages, understand the tk grids, made a testing subclass,
write a grid example.  The other items are still on my queue and I am
actively avoiding those items with low risk.

In the short term, I'll bring up Travis CI to get some build clarity,
look at the Futures project for 2.x, 3.x compatibility, and figure out
the HTML version.



Wednesday, March 19, 2014
===

Haven't been updating for a little while.  I spent a fun day updating
my keyboard mappings to handle using the space bar a control key.  On
the code, I'm both hung up on the tk grid control and on the need to
do some refactoring.  Each subclass should implement its own logic for
the walk through the spec, but I want to have the identification and
chunking of the spec in a common place.  It's time to get the code
into a more useful and testable form.  Time to break apart the
modules.  Overall, my list of things to do with the code has gotten
long enough it becomes tempting to put it aside.

So here is the list: break out packages, rewrite the basic render
logic, understand tk grids, make a testing subclass so I can write
some tests, make many more usage examples, write an example for tk
grid, write an example for add_two in flask, make a flask target,
≤figure out how to test guis.

It's an odd time for a project.  So, first step, get things into git.
Second, work to have tests and builds do something.  Third, try to
test what I have.  Then add.  I find I first want to much with my
editor and made it use the system clipboard.

So, let's start with git.  Then make all.  Also, I need to rethink github.




Sunday, March 9, 2014
-

Grabbed a bit of time during Andrew's gaming party.  Working through
the tkInter tutorials and writing tk_ programs in the overly
documented style.

Still thinking about how this should be tested.  Starting with a tk
only implementation.

Learned that epylint is utterly cracked.  For example, "epylint -E
*.py" is an error, but "epylint *.py -E" is not.  Both pylint and epylint
seemed cracked about not looking in the python source directory for the
imports.

Saturday, March 8, 2014
-

Started the project.  CoffeeSociety's internet connection went down,
so I could create the PyUI repository there.  Still, the first step is
an exercise in getting the system running.  I don't expect to use
docker on this until later.

Added a basic makefile to have blank tests that pass.  First step.

Need to start a module I guess.

Spent an hour on devEnv again.   Still can't get pylint doing the right thing.

Linked a readme to the plan doc.  Added integration test to makes.

Even though HFS+ is not case sensitive, the import statement is.
