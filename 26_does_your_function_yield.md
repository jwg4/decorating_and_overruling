>>> def some_points(n):
...     for i in range(0, n):
...         yield 'a'
... 
>>> some_points(1)
<generator object some_points at 0x7f90a49540a0>
>>> list(some_points(1))
['a']
>>> list(some_points(0))
[]
>>> list(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not iterable
>>> def return_nothing(n):
...     return
... 
>>> list(return_nothing(0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not iterable
>>> def some_points_and_return(n):
...     for i in range(0, n):
...         yield 'a'
...     return
>>> list(some_points_and_return(0))
[]
>>> def never_any_points_and_return(n):
...     if True is False:
...             yield 'a'
...     return
... 
>>> list(never_any_points_and_return(5))
[]

This affects looping over the results of functions:
>>> def function_with_yield():
...     if True is False:
...             yield
...     return
... 
>>> for i in function_with_yield():
...     print 'Hello'
... 
>>> def function_without_yield():
...     return
... 
>>> for i in function_without_yield():
...     print 'Hello'
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not iterable

