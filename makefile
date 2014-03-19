# Note 'all' must be the first target.
# Note the '@' at the beginning of @echo means don't display command

all:   environment lint tests
	@echo "All tests pass"

test_pass:
	@echo "Empty test passes!"

test_add_two:
	cd src && python add_two.py

# This is here just to have a failed make.  It is not in the test list.
test_fail:
	@echo "Should fail" && /usr/bin/false

tests:  test_pass nosetest test_add_two

nosetest:
	nosetests src/pyUI.py

environment:
	source ~/.virtualenvs/big3/bin/activate

lint:
	# TODO:  figure out flymake or just get this to run epylint src/*.py
	cd src && epylint add_two.py -E   # look for errors first
	cd src && epylint add_two.py -r n || true  # show warnings but continue
