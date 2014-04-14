""" A simple program to test adding two numbers.

This should kick out some html, serve it, and handle a post that changes
the numbers.  On the post, it should return to the calling program so that
a total page can be served.

This means:

basic template
add_fields_to_template
html_for_enter_values
add_total_field
html_for_show_total

with infrastructure of:
a template engine
an http server

"""
