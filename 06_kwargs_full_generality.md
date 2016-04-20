The fullest generality of using * and ** in function definitions can involve
combining explicit named and unnamed arguments with a list of further unnamed arguments
and a dict of further named arguments.

>>> def print_argument_info(first, second, third, fourth, *args, **kwargs):
...     print first
...     print str(second) + '!'
...     print '(%s -- %s)' % (third, fourth)
...     print ', '.join(args)
...     print len(kwargs), kwargs.keys(), str(kwargs)

>>> print_argument_info(1, 2, 3, 4)
1
2!
(3 -- 4)
<BLANKLINE>
0 [] {}

>>> print_argument_info(1, 2, 3, 4, 'hello', 'world')
1
2!
(3 -- 4)
hello, world
0 [] {}
