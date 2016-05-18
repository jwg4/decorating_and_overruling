Suppose that we want to create a decorator which can be used on function with any set of arguments.

We can use 'args' and 'kwargs' to do so, since any function can have its arguments expressed using those two.

>>> def stringify(original_function):
...     def new_function(*args, **kwargs):
...         return str(original_function(*args, **kwargs))
...
...     return new_function

>>> @stringify
... def multiply_by_three(x):
...     return x * 3

>>> multiply_by_three(10)
'30'

>>> import string
>>> @stringify
... def my_split(s, sep, maxsplit=-1):
...     return string.split(s, sep, maxsplit)

>>> my_split('Not a pleasant pheasant plucker.', 'p', maxsplit=4)
"['Not a ', 'leasant ', 'heasant ', 'lucker.']"

Decorators are just functions which act on functions, and decorating a function is just syntactic sugar. We could do the same by defining a function and then redefining it.

>>> from datetime import date, timedelta

>>> def add_three_days(dt):
...     return dt + timedelta(days=3)

>>> add_three_days = stringify(add_three_days)

>>> add_three_days(date(2012, 10, 30))
'2012-11-02'

We could equally invoke a decorator without using it to decorate - we don't have to assign the transformed function back to the same name.

>>> from math import tan, pi, sin

>>> stringified_tan = stringify(tan)

>>> stringified_tan(pi/4)
'1.0'

Or even
>>> stringify(sin)(0.0)
'0.0'
