The usual way of specifying argument is as a tuple of names.
Each name will have a value only in scope of the function while it is being evaluated.

>>> def fun(b, f, h):
...     print b
...     n = f + h
...     return n

Arguments can be made optional by giving a name and a default value:
>>> def add_two_numbers(x, y=0):
...     return x + y

>>> add_two_numbers(3, 4)
7
>>> add_two_numbers(3)
3

There can be more than one optional argument, but they all have to come at the end of the list of arguments:
>>> def evaluate_polynomial(x, a0, a1=0, a2=0, a3=0, a4=0, a5=0):
...     return a5 * x**5 + a4 * x**4 + a3 * x**3 + a2 * x**2 + a1 * x + a0
>>> evaluate_polynomial(2, 1, 1, 1, 1, 1, 1)
63
>>> evaluate_polynomial(0.5, 17)
17.0
>>> evaluate_polynomial(-1, 1, 2, 1)
0
