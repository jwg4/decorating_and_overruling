>>> def transform(x):
...     return sorted(x)

>>> def fn(x):
...     y = transform(x)
...     return munge(y)

>>> def munge(a, **kwargs):
...     return "foo %s bar %s baz" % (a, kwargs)

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
    "foo aaddffss bar {u"w": u"wozzat", u"k": u"keyber"} baz"

