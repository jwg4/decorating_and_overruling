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
