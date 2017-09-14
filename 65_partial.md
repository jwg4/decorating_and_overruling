From the functools built-in package, `partial` is a function which 'partially evaluates' functions. This means taking a function of multiple arguments and some of the arguments, and creating a function which needs the missing arguments, but has the other arguments 'pre-set'.

```
>>> from functools import partial

>>> def f(x, y):
...     return x + y
...
>>> f(2, 3)
5

```

```
>>> g = partial(f)
>>> g  # doctest: +ELLIPSIS
<functools.partial object at 0x...>
>>> g()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 2 arguments (0 given)
>>> g(1, 2)
3

```

```
>>> h = partial(f, 10)
>>> h  # doctest: +ELLIPSIS
<functools.partial object at 0x...>
>>> h()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 2 arguments (1 given)
>>> h(4)
14
>>> h(6)
16

```

```
>>> j = partial(f, 7, 7)
>>> j  # doctest: +ELLIPSIS
<functools.partial object at 0x...>
>>> j()
14
>>> j(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 2 arguments (3 given)

```

We could use partial on a function which doesn't have any arguments, although it doesnt seem very useful:

```
>>> def do_something():
...     print("Hello")
>>> do_something()
Hello
>>> new_version = partial(do_something)
>>> new_version  # doctest: +ELLIPSIS
<functools.partial object at 0x...>
>>> new_version()
Hello

```

The new function behaves exactly the same as the original one.

Everything that we can do with partial, we could also do with lambdas, or with def, and a function which returns a function. Partial makes a common manipulation much easier.