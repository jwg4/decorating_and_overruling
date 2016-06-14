>>> def natural_numbers():
...     i = 0
...     while True:
...             yield i
...             i = i + 1
... 
>>> natural_numbers()
<generator object natural_numbers at 0x7f922facc0f0>
>>> list(natural_numbers())
^C^Z
[1]+  Stopped                 python