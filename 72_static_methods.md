>>> class Dog(object):
...     @staticmethod
...     def do_something():
...         print "Called this method."
...
>>> Dog.do_something()
Called this method.
>>> x = Dog()
>>> x.do_something()
Called this method.