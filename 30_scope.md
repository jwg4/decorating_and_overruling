>>> def a_function(optional=None):
...     print optional

>>> a_function('foo')
foo
>>> a_function()
None

>>> def another_function(optional=None):
...     if optional is not None:
...         print optional

>>> another_function('foo')
foo
>>> another_function()

>>> def yet_another_function(optional=None):
...     if optional is None:
...         optional = 'default'
...     print optional

>>> yet_another_function('foo')
foo
>>> yet_another_function()
default

>>> x = 4
>>> def function_using_variable_from_global_scope():
...     print x

>>> function_using_variable_from_global_scope()
4

>>> def function_overwriting_variable_from_global_scope():
...     if y is None:
...         y = 'default'

>>> function_overwriting_variable_from_global_scope()
Traceback (most recent call last):
...
UnboundLocalError: local variable 'y' referenced before assignment

>>> y = None
>>> function_overwriting_variable_from_global_scope()
Traceback (most recent call last):
...
UnboundLocalError: local variable 'y' referenced before assignment

>>> y = 'asdf'
>>> function_overwriting_variable_from_global_scope()
Traceback (most recent call last):
...
UnboundLocalError: local variable 'y' referenced before assignment
