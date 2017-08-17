>>> def f(x):
...     return x + 2
... 
>>> def apply(f, a):
...     return lambda: f(a)
... 
>>> apply(f, 3)
<function <lambda> at 0x7f93e1211cf8>
>>> apply(f, 3)()
5
