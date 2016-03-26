The purpose of this file is as follow: we have the two functions
munge and transform:
>>> def transform(x):
...     return sorted(x)

>>> def munge(a, **kwargs):
...     return "foo %s bar %s baz" % (a, kwargs)

They are quite straightforward, and we make some basic tests on their operation:
>>> transform([2, 3, 1])
[1, 2, 3]

>>> transform('zloty')
['l', 'o', 't', 'y', 'z']

>>> munge('boosh')
'foo boosh bar {} baz'

>>> munge('boosk', b='one', c='two')
"foo boosk bar {'c': 'two', 'b': 'one'} baz"

Another function uses both of these to do something:
>>> def fn(x):
...     y = transform(x)
...     return munge(y)

>>> fn('egbdf')
"foo ['b', 'd', 'e', 'f', 'g'] bar {} baz"

This function always calls munge() with a single argument. There is
no way for us to pass in extra arguments to fn which will get used 
in the call to munge(). If we can't change fn(), it seems like we 
have no way of making sure munge gets called with more than one argument.

What we want fn to do:
>>> munge(transform([4, 5, 1]), b=13, c=37)
"foo [1, 4, 5] bar {'c': 37, 'b': 13} baz"

What definitely won't work:
>>> fn([4, 5, 1], b=13, c=37)
Traceback (most recent call last):
  ...
TypeError: fn() got an unexpected keyword argument 'b'

However, we try to construct a decorator that will do this:
>>> def decorator(f):
...     def g(x):
...         global munge
...         old_munge = munge
...         munge = dict
... 
...         old_ret = f(x)
...         z = dict(w="wozzat", k="keyber")
...         return old_munge(old_ret, **z)
...     return g

>>> decorated = decorator(fn)

>>> decorated("asdfasdf")
"foo ['a', 'a', 'd', 'd', 'f', 'f', 's', 's'] bar {'k': 'keyber', 'w': 'wozzat'} baz"

