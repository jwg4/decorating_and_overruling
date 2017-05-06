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