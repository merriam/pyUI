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
