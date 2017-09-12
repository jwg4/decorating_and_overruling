>>> from functools import partial
>>> def f(x, y):
...     return x + y
...
>>> f(2, 3)
5
>>> g = partial(f)
>>> g()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 2 arguments (0 given)
>>> g(1, 2)
3
>>> h = partial(f, 10)
>>> h
<functools.partial object at 0x7efd384d2310>
>>> h()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 2 arguments (1 given)
>>> h(4)
14
>>> h(6)
16
>>> j = partial(f, 7, 7)
>>> j
<functools.partial object at 0x7efd384d2368>
>>> j()
14
>>> j(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 2 arguments (3 given)
