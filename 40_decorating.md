Suppose that we have a function which takes a function as argument and returns another function
>>> def make_a_double_evaluator(fn):
...     def do_it_twice():
...         fn()
...         fn()
...     return do_it_twice

We can see this functional as a transformation which acts on functions
>>> def print_hello_world():
...     print 'Hello World!'
>>> print_hello_world()
Hello World!

>>> f = make_a_double_evaluator(print_hello_world)
>>> f()
Hello World!
Hello World!

We could assign the result of this transformation to the original function:
>>> print_hello_world = make_a_double_evaluator(print_hello_world)
>>> print_hello_world()
Hello World!
Hello World!

(We could even do this more than once..)
>>> print_hello_world = make_a_double_evaluator(print_hello_world)
>>> print_hello_world()
Hello World!
Hello World!
Hello World!
Hello World!

Decorators do exactly this, at the point of defining a function.
They take the function just defined, pass it to some other specified function, take the return value, and assign it to the name of the original function
>>> @make_a_double_evaluator
... def print_foo():
...     print 'Foo'

>>> print_foo()
Foo
Foo
