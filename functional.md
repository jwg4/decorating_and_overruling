In Python functions can be passed as arguments to functions:

>>> def evaluate_at_4(f):
...     return f(4)

>>> from math import sqrt
>>> evaluate_at_4(sqrt)
2.0

