# What is a keyword?

We can't use a string as an argument name.

```
>>> def f(x, y, **kwargs):
...     print(kwargs)

>>> f(1, 2, Hello World=3)
SyntaxError

```
