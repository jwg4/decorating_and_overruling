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
