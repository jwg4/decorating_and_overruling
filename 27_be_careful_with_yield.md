>>> def natural_numbers():
...     i = 0
...     while True:
...             yield i
...             i = i + 1
... 
>>> natural_numbers() # doctest: +ELLIPSIS
<generator object natural_numbers at 0x...>

The following code cannot be run as a doctest since it will overwhelm the process. But it is the real output of a python REPL:
#  >>> list(natural_numbers())
#  ^C^Z
#  [1]+  Stopped                 python


More code which can't be run:
>>> def generate_once():
...     yield 1
... 
>>> generate_once() # doctest: +ELLIPSIS
<generator object generate_once at 0x...>
>>> import sys
>>> sys.exit() for x in generate_once()
Exception raised:
    Traceback (most recent call last):
    File "<stdin>", line 1
    sys.exit() for x in generate_once()
                 ^
SyntaxError: invalid syntax
>>> (sys.exit() for x in generate_once()) # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>
>>> foo = (sys.exit() for x in generate_once())

This line will exit python:
#  >>> list(foo)
