The usual way of specifying argument is as a tuple of names.
Each name will have a value only in scope of the function while it is being evaluated.

>>> def fun(b, f, h):
...     print b
...     n = f + h
...     return n

Arguments can be made optional by giving a name and a default value:
>>> def add_two_numbers(x, y = 0):
...     return x + y

>>> add_two_numbers(3, 4)
7
>>> add_two_numbers(3)
3
