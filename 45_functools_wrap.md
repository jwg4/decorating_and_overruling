The built-in library `functools` contains several utility functions for working with functions.
See https://docs.python.org/2/library/functools.html
One of the most important is `partial`, which we will see later.

Here we look at `wraps`, which makes decorators work in a slightly more convenient way.
First let's try and create a decorator which might be useful. This one takes a function and turns it
into a function which can deal with None being passed in.

```
>>> def protect_from_none(f):
...     def temp(x):
...         if x is None:
...             return None
...         return f(x)
...     return temp

```

We take a function which we could apply it to:
```
>>> def add_five(n):
...     """ Adds five to things. """
...     return n + 5
...
>>> add_five(10)
15
>>> add_five(None)
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

```

Let's check some of the details of how this function is represented:

```
>>> add_five  # doctest: +ELLIPSIS
<function add_five at 0x...>
>>> add_five.__doc__
' Adds five to things. '

```

Now let's define the function again, this time using the decorator.

```
>>> @protect_from_none
... def add_five(n):
...     """ Adds five to things. """
...     return n + 5
...
>>> add_five(2)
7
>>> add_five(None)

```

It works, but we have messed up some of the metadata of the function a bit.

```
>>> add_five  # doctest: +ELLIPSIS
<function temp at 0x...>
>>> add_five.__doc__

```

To keep this metadata in the decorated function, we use `wraps` in the decorator.

```
>>> from functools import wraps
>>> def protect_from_none(f):
...     @wraps(f)
...     def temp(x):
...         if x is None:
...             return None
...         return f(x)
...     return temp

```

When we defined the function `temp`, we specified that it was supposed to be a replacement for `f`.

```
>>> @protect_from_none
... def add_five(n):
...     """ Adds five to things. """
...     return n + 5
...
>>> add_five  # doctest: +ELLIPSIS
<function add_five at 0x...>
>>> add_five.__doc__
' Adds five to things. '

```