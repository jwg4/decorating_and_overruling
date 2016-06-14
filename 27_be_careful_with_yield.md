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
