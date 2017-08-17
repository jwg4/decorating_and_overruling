This is a clever piece of code which is designed to make recursive functions work even where the stack depth would become too big. Taken from https://github.com/mattneary/Thunctor

First, let's take an example of where we can't recurse deeply enough:
>>> def power_of_two(n):
...     if n == 0:
...         return 1
...     return 2 * power_of_two(n-1)
...
>>> power_of_two(4)
16
>>> power_of_two(1000)
Traceback (most recent call last):
 ...
RuntimeError: maximum recursion depth exceeded


This example is in some way the dual of the one in file 95. There we used functions and function evaluation to create a data structure which looks like a list. Here we use a list to store functions, rather than simply evaluate our way through the stack of functions.
