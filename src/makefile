# Makefile for pyui src and tests.
# Note 'all' must be the first target so a bare '$ make' does 'all'.
# Note the '@' at the beginning of @echo means don't display command

all:   environment tests
	@echo "All tests pass"

test_pass:
	@echo "Empty test passes!"

test_add_two:   environment
	python add_two.py

# This is here just to have a failed make.  It is not in the test list.
test_fail:
	@echo "Should fail" && /usr/bin/false

tests:  test_pass nosetest test_add_two

nosetest:  environment
	nosetests add_two.py pyUI/*.py

environment:
	# Yes, I hardcoded this path; makes life simple right now.
	cd ~/p/pyui
	source ~/.virtualenvs/big3/bin/activate

lint:	environment
	# TODO:  figure out flymake or just get this to run epylint *.py
	epylint add_two.py -E   # look for errors first
	epylint add_two.py -r n || true  # show warnings but continue
