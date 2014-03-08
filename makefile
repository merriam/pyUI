# Note 'all' must be the first target.
# Note the '@' at the beginning of @echo means don't display command

all:   tests
	@echo "All tests pass"

test_pass:
	@echo "Empty test passes!"

# This is here just to have a failed make.  It is not in the test list.
test_fail:
	echo "Should fail" && /usr/bin/false

tests:  test_pass
