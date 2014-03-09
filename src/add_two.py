""" Simple integration test to add two numbers """
import pyui as ui
fields = [["Enter first number:", "{int number1}"],
          ["Enter second number", "{int number2}"]]
output = ui.dialog(fields)
total = output["number1"] + output["number2"]
output = ui.dialog("Total value is " + total)
