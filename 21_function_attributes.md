Not just the __doc__ attribute but arbitrary attributes of functions can be set.

>>> def f(x):
...     return x + 3

>>> f(4)
7
>>> f  # doctest: +ELLIPSIS
<function f at 0x...>
>>> f.foo = 'whatever'
>>> f  # doctest: +ELLIPSIS
<function f at 0x...>
>>> f.foo
'whatever'
>>> g = f
>>> g  # doctest: +ELLIPSIS
<function f at 0x...>
>>> g(12)
15
>>> g.foo
'whatever'

Attributes of functions can be any type of object: lists, class instances, other functions...
>>> f.asdf = ["Q", "W", "E", "R", "T", "Y"]
>>> f.blah = g


One way of checking what attributes are set is to use __dict__
>>> hello.__dict__()
{}

>>> import datetime
>>> hello.foo = datetime.datetime(2017, 4, 27, 1, 1, 1)
>>> hello.__dir__()
{'foo': datetime.datetime(2017, 4, 27, 1, 1, 1)
