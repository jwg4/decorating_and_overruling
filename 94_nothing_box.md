```
>>> import sys
>>> def f():
...     name = sys._getframe().f_code.co_name
...     globals().pop(name)
...
>>> f()
>>> f()
Traceback (most recent call last):
  ...
NameError: name 'f' is not defined

```
