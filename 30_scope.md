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
