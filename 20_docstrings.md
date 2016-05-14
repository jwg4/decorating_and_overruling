The definition of a function can include a *docstring*, a quoted string which is the first thing in the function declaration:
>>> def next_month(year, month):
...     """Given a month and a year, returns the following month."""
...     if month == 12:
...         return (year + 1, 1)
...     return (year, month + 1)

>>> next_month(2010, 8)
(2010, 9)
>>> next_month.__doc__
'Given a month and a year, returns the following month.'

Functions also have a built-in attribute __name__, the name of the function.
>>> next_month.__name__
'next_month'

Both __doc__ and __name__ can be changed outside of the function definition.
>>> next_month.__name__ = 'my_new_function_name'

>>> next_month.__name__
'my_new_function_name'

Reassigning the name does not mean that a function with that name is defined:
>>> my_new_function_name(2012, 10)
Traceback (most recent call last):
...
NameError: name 'my_new_function_name' is not defined
