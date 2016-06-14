>>> def natural_numbers():
...     i = 0
...     while True:
...             yield i
...             i = i + 1
... 
>>> natural_numbers() # doctest: +ELLIPSIS
<generator object natural_numbers at 0x...>

>>> list(natural_numbers())
^C^Z
[1]+  Stopped                 python
