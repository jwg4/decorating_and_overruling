Many Python objects have an attribute called '__call__', which is what is needed to use the 'brackets' operator on a thing.

>>> def fn(x):
...     return 4

>>> class Foo(object):
...     pass

>>> foo = Foo()
>>> foo()
Traceback (most recent call last):
  ...
TypeError: 'Foo' object is not callable

>>> class Foo(object):
...     __call__ = fn

>>> foo = Foo()
>>> foo()
4

