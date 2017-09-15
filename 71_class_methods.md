```
>>> class Dog(object):
...     @classmethod
...     def do_something(cls):
...         print "Called this method."
...
>>> Dog.do_something()
Called this method.
>>> x = Dog()
>>> x.do_something()
Called this method.

```

```
>>> class Foo(object):
...     def bar(self, x):
...         return x + 4
...
>>> foo = Foo()
>>> foo.bar(3)
7
>>> f = foo.bar
>>> f(3)
7

```
