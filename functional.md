In Python functions can be passed as arguments to functions:

>>> def evaluate_at_4(f):
...     return f(4)

>>> from math import sqrt
>>> evaluate_at_4(sqrt)
2.0

>>> def repeat_x(n):
...     return 'x' * n
>>> evaluate_at_4(repeat_x)
'xxxx'

Functions can also return functions:

A trivial example:
>>> def create_a_simple_function():
...     def simple_function():
...         print 'foo'
...     return simple_function

>>> my_function = create_a_simple_function()
>>> my_function()
foo

You can call the returned function directly:
>>> create_a_simple_function()()
foo

But you can't directly call the function as defined inside create_a_simple_function()
>>> simple_function()
Traceback (most recent call last):
 ...
NameError: name 'simple_function' is not defined
