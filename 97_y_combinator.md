```
>>> def Y(f):
...     def a(x):
...         return f(x(x))
...     
...     return a(a)

```

```
>>> def my_fun(x):
...     return -1.0 / x

```

>>> my_fun(4)
-0.25

>>> Y(my_fun)
Traceback (most recent call last):
 ...
RuntimeError: maximum recursion depth exceeded
