The usual way of specifying argument is as a tuple of names.
Each name will have a value only in scope of the function while it is being evaluated.

>>> def fun(b, f, h):
...     print b
...     n = f + h
...     return n
