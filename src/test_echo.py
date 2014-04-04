import pyui
import re

def check_echo(spec_thing, regex_list):
    output = pyui.Echo().dialog(spec_thing)
    assert output and "echo" in output
    for regex in regex_list:
        assert re.search(regex, output["echo"]), "Cannot match {} in {}".format(regex, output["echo"])
        pass   # probably unnecessary, but unclear if odd compiler flags are used.

def test_echo_add_two():
    fields = [["Enter first number:", ":number1 is number"],
              ["Enter second number", ":number2 is number"]]
    regexes = ["Adding label Enter first number",
               "grid item at \(1\, 1\)",
               "\W+3\:\W+Adding entry number2"]
    check_echo(fields, regexes)
