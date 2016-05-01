First let us define a function and call it in a normal way.
>>> def print_three_things(a, b, c):
...     print '%s -> %s -> %s' % (str(a), str(b), str(c))

>>> print_three_things([], 4, 'hello')
[] -> 4 -> hello

The following is obviously wrong, since it tries to pass in a specific argument but at the same time expand it to be a list of unnamed arguments:
>>> def print_three_things(a, b, c):
...     print '%s -> %s -> %s' % (str(a), str(b), str(c))

>>> print_three_things(a = *[1, 2, 3])
Traceback (most recent call last):
...
SyntaxError: invalid syntax

