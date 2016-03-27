In Python functions can be passed as arguments to functions:

>>> def evaluate_at_4(f):
...     return f(4)

>>> from math import sqrt
>>> evaluate_at_4(sqrt)
2.0

>>> def repeat_x(n):
...     return 'x' * n
>>> evaluate_at_4(repeat_x)
'xxxx'

Functions can also return functions:

A trivial example:
>>> def create_a_simple_function():
...     def simple_function():
...         print 'foo'
...     return simple_function

>>> my_function = create_a_simple_function()
>>> my_function()
foo

You can call the returned function directly:
>>> create_a_simple_function()()
foo

But you can't directly call the function as defined inside create_a_simple_function()
>>> simple_function()
Traceback (most recent call last):
 ...
NameError: name 'simple_function' is not defined

You can also assign a function to a variable. As usual in Python, you don't have 
to do anything special to express the type of 'thing' stored by the variable.
>>> my_var = max
>>> my_var(10, 20, 30)
30

We already saw how this was done with a function return value:
>>> a = create_a_simple_function()
>>> a()
foo

Notice that we can assign the contents of 'a' to another variable:
>>> b = a
>>> b()
foo

And in general, store that function in various ways:
>>> d = [1, 3.14, 'blah', create_a_simple_function() ]
>>> d[3]()
foo
>>> my_dict = { 'g': [1, 2, 3], 'h': b }
>>> my_dict['h']()
foo

We can also use variables to pass functions into a function:
>>> y = float
>>> evaluate_at_4(y)
4.0

>>> def say_hello_n_times(n):
...     for i in range(n):
...         print 'hello'
>>> w = say_hello_n_times
>>> evaluate_at_4(w)
hello
hello
hello
hello
