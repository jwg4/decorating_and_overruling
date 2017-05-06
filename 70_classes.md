Classes are the basis of object-oriented programming in Python. The typical class contains an (optional) initializer and some methods.

>>> class Car(object):
...     def __init__(self):
...         print 'Initializing a Car.'
...         self.speed = 0
...
...     def drive(self):
...         print 'Driving a Car.'
...         self.speed = self.speed + 5
...         return self.speed

When we create an instance of the Car class, the initializer is called:
>>> x = Car()
Initializing a Car.

We could if we wanted to call it at some other time:
>>> x.__init__()
Initializing a Car.

This is the syntax we typically use to call other class methods than the initializer:
>>> x.drive()
Driving a Car.
5

When we invoke a member method (using the . operator), the function is called, passing in the object in question as the first argument. 

We could call the function directly, provided that we identify the function using the name of the class.
>>> Car.drive(x)
Driving a Car.
10

So x.drive() is syntactic sugar which does two things: identify the function drive() which belongs to x's type, and call it with x as the first parameter. The error messages reflect the number of parameters, including the implicit self.

>>> Car.drive()
Traceback (most recent call last):
 ...
TypeError: drive() missing 1 required positional argument: 'self'

>>> x.drive(4)
Traceback (most recent call last):
 ...
TypeError: drive() takes 1 positional argument but 2 were given