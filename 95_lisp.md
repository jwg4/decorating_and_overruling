>>> def cons(a, b):
...     def return_first_or_second(n):
...         if n == 1:
...             return a
...         if n == 2:
...             return b
...     return return_first_or_second

>>> def car(l):
...     return l(1)

>>> def cdr(l):
...     return l(2)

>>> x = cons(1, cons(2, cons(3, 4)))
>>> x # doctest: +ELLIPSIS
<function return_first_or_second at 0x...>
>>> car(cdr(x))
2
