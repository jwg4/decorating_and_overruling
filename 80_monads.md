Monads are transformations which can be made to functions, to make them act more like pieces of arbitrary imperative code.

How imperative code works is that any collection of instructions can follow any other, and there is some global state which 'knows' what has already happened and how it affected things. The difference between this and functional code is that in functional code, ultimately everything we do has to be a single function evaluation, where the arguments might be the results of other evaluations and so on. Monads 'combine' functions so that the evaluation of one function might seen like it is 'following' and therefore 'affected by' the evaluation of another.

>>> class Maybe(object):
...     def __init__(self, thing):
...         self.thing = thing
...         self.is_none = (thing is None)
...
...     def __repr__(self):
...         if self.is_none:
...             return 'Nothing'
...         return 'Maybe(%s)' % self.thing

>>> def _bind(f):
...     def new_f(a):
...         if a.is_none:
...             return Maybe(None)
...         return f(a.thing)
...
...     return new_f

>>> from math import log

>>> @_bind
... def safe_log(x):
...     if x > 0:
...         return Maybe(log(x))
...     return Maybe(None)

>>> safe_log(safe_log(safe_log(Maybe(1.0))))
Nothing

>>> safe_log(safe_log(safe_log(Maybe(10.0))))
Maybe(-0.181482974205)
