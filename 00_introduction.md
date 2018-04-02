These are worked examples - you can read through them, copy them into a Python terminal to try them out, or you can run doctest to make sure they all work as explained.

As long as you have seen functions before in Python, you should be able to follow from the start. 
But let's review a little about how doctest works.
In general the doctest pieces should look exactly like an interactive Python session.

Code which is to be run starts with '>>>'
>>> import json

Blocks are continued with lines that start with '...', and are otherwise indented as usual:
>>> def function(x):
...     return 'foo'

If the expression being evaluated returns something, it will be printed on the next line.
>>> 2 + 2
4

If it returns a string, this will be displayed in quotes
>>> 'asdf' + 'qwer'
'asdfqwer'

On the other hand, code which prints something will show the output without quotes:
>>> print 'Hello, world!'
Hello, world!

Exceptions are displayed like the output you would see normally when an exception is raised, except that the stack trace is replaced by three dots:
>>> prinj 'Hello, world!'
Traceback (most recent call last):
 ...
SyntaxError: invalid syntax

Finally, if an expression evaluates to None, nothing is displayed.
>>> None

You can check for None eg. by doing str().
>>> x = None
>>> x
>>> str(x)
'None'
>>> x is None
True
