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

Why does this happen? Because if there is an assignment to a variable inside a scope, then the Python compiler assumes that the variable is local to that scope. So in the first function the compiler correctly looks for the declaration of x in the outer scope, but in the second case it ignores this, and assumes that x is a new variable, local to inner().

This is done to protect you, in case you have:
>>> import date

and then (maybe thousands of lines later:
>>> def parse_data(s):
...     date = s.split('/')[:3]
...     return date

You obviously don't want the global meaning of the symbol date, so it is ignored for the length of that function.
