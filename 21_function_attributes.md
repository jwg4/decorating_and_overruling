Not just the __doc__ attribute but arbitrary attributes of functions can be set.

>>> def f(x):
...     return x + 3
... 
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
One way of checking what attributes are set is to call __dir__
>>> g.__dir__()
['foo', '__repr__', '__call__', '__get__', '__new__', '__closure__', '__doc__', '__globals__', '__module__', '__code__', '__defa
ults__', '__kwdefaults__', '__annotations__', '__dict__', '__name__', '__qualname__', '__hash__', '__str__', '__getattribute__',
 '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduc
e__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']