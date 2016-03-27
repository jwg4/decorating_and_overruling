Skip this section if you are pretty confident you remember how functions are defined and called in Python

We define a function using def
>>> def add_two(n):
...     return n + 2

And call it using the brackets operator
>>> add_two(3)
5

Some functions do not have arguments
>>> def do_something():
...     return 'We are done'

>>> do_something()
'We are done'

Some functions have several arguments
>>> def complicated_calculation(a, b, c):
...     d = a * b + 2 * c
...     return d + c / a

>>> complicated_calculation(1, 2, 3)
11
