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
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in power_of_two
  File "<stdin>", line 4, in power_of_two
  File "<stdin>", line 4, in power_of_two
  [Previous line repeated 994 more times]
  File "<stdin>", line 2, in power_of_two
RecursionError: maximum recursion depth exceeded in comparison
