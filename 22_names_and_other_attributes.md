Functions have a name, and the name is set at the time of defining the function.
>>> def hello(person):
...     print "Hello %s" % person

>>> hello  # doctest: +ELLIPSIS
<function hello at 0x...>

If we assign this function to another variable, it still keeps its original name.
>>> greet = hello

>>> greet("Sophie")
Hello Sophie

>>> greet  # doctest: +ELLIPSIS
<function hello at 0x...>

However, we can change the name
>>> greet.__name__ = "my_fn"

>>> greet  # doctest: +ELLIPSIS
<function my_fn at 0x...>

Because there is really only one function, and two variables which point to it, the original function changes name too.
>>> hello  # doctest: +ELLIPSIS
<function my_fn at 0x...>

One way of checking what attributes are set is to call __dir__
>>> hello.__dir__()
Traceback (most recent call last):
 ...
AttributeError: 'function' object has no attribute '__dir__'

>>> import datetime
>>> hello.foo = datetime.datetime(2017, 4, 27, 1, 1, 1)
>>> hello.__dir__()
['foo', '__repr__', '__call__', '__get__', '__new__', '__closure__', '__doc__', '__globals__', '__module__', '__code__', '__defa
ults__', '__kwdefaults__', '__annotations__', '__dict__', '__name__', '__qualname__', '__hash__', '__str__', '__getattribute__',
 '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduc
e__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']