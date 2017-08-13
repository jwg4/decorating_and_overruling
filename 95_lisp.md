This is an example of how we can create CONS, CAR and CDR, the building blocks of LISP, in Python. We don't use Python lists to do this, but construct the data structures using only functions which return functions. This is the way shown in SICP https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs (Actual LISP implementations typically do not use this trick.) 

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
A 'list' is actually a function.
>>> x # doctest: +ELLIPSIS
<function return_first_or_second at 0x...>
We haven't set up any way of prettily printing the contents of the list.
>>> car(cdr(x))
2
But the individual elements are just the Python types we put into the list.
