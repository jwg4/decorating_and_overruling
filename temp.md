A gotcha involving global and local scope:
>>> def print_a_thing(x=None):
...     def inner():
...         print x
...     return inner
... 

>>> def print_a_thing_with_a_default(x=None):
...     def inner():
...         if x is None:
...             x = 1
...         print x
...     return inner
... 

>>> print_a_thing()()
None

>>> print_a_thing(5)()
5

>>> print_a_thing_with_a_default()()
Traceback (most recent call last):
  ...
UnboundLocalError: local variable 'x' referenced before assignment

>>> print_a_thing_with_a_default(5)()
Traceback (most recent call last):
  ...
UnboundLocalError: local variable 'x' referenced before assignment
