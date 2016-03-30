Suppose we want to have, not a fixed number of arguments, of which some can be omitted, but a list of arbitrarily many arguments.
The * notation for arguments allows us to read in such a list.

>>> def sum_many_numbers(*numbers):
...     x = 0
...     for n in numbers:
...         x = x + n
...     return x

>>> sum_many_numbers(1)
1
>>> sum_many_numbers(1, 1, 2)
4
>>> sum_many_numbers(1, 0.5, 0.25, 0.125, 0.0625)
1.9375
>>> sum_many_numbers()
0

Note that passing in an actual list will not work correctly:
>>> sum_many_numbers([0, 1])
Traceback (most recent call last):
 ...
TypeError: unsupported operand type(s) for +: 'int' and 'list'

