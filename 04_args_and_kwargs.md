Suppose we want to have, not a fixed number of arguments, of which some can be omitted, but a list of arbitrarily many arguments.
The * notation for arguments allows us to read in such a list.

>>> def sum_many_numbers(*numbers):
...     x = 0
...     for n in numbers:
...         x = x + n
...     return x

>>> sum_many_numbers(1)
1
>>> sum_many_numbers(1, 1, 2)
4
>>> sum_many_numbers(1, 0.5, 0.25, 0.125, 0.0625)
1.9375
>>> sum_many_numbers()
0

Note that passing in an actual list will not work correctly:
>>> sum_many_numbers([0, 1])
Traceback (most recent call last):
 ...
TypeError: unsupported operand type(s) for +: 'int' and 'list'

However, you can pass in a list of all the individual arguments, by using * when you call the function.
>>> sum_many_numbers(*[0, 1])
1

This use of the * notation also works for functions which are defined in the normal way:
>>> def sum_three_numbers(first, second, third):
...     return first + second + third

>>> sum_three_numbers(*[10, 11, 12])
33
>>> sum_three_numbers(*[10, 11, 12, 13])
Traceback (most recent call last):
 ...
TypeError: sum_three_numbers() takes exactly 3 arguments (4 given)
>>> sum_three_numbers(*[])
Traceback (most recent call last):
 ...
TypeError: sum_three_numbers() takes exactly 3 arguments (0 given)

Got that? * when you define the function, means 'take the arguments, and put them into a list'.
* when you call the function, means 'take this list, and use the members as successive arguments'.
Using * in the definition doesn't mean you do or don't have to use it in the call, and vice versa.
