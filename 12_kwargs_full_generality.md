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

We can add extra unnamed arguments.
>>> print_argument_info(1, 2, 3, 4, 'hello', 'world')
1
2!
(3 -- 4)
hello, world
0 [] {}

We can also use a shorter list of unnamed arguments, and provide some arguments using named arguments.
>>> print_argument_info(1, 2, fourth=3, third=4)
1
2!
(4 -- 3)
<BLANKLINE>
0 [] {}

We can also add some extra named arguments, whether alongside some required named arguments, or only unnamed arguments.
>>> print_argument_info(1, 2, fourth='boo', third='bar', y='baz', foo_level='foo')
1
2!
(bar -- boo)
<BLANKLINE>
2 ['y', 'foo_level'] {'y': 'baz', 'foo_level': 'foo'}

>>> print_argument_info(1, 2, 'boo', 'bar', y='baz', foo_level='foo')
1
2!
(boo -- bar)
<BLANKLINE>
2 ['y', 'foo_level'] {'y': 'baz', 'foo_level': 'foo'}

We could also combine additional named and additional unnamed arguments:
>>> print_argument_info(1, 2, 3, 4, 'hello', 'world', y='baz', foo_level='foo')
1
2!
(3 -- 4)
hello, world
2 ['y', 'foo_level'] {'y': 'baz', 'foo_level': 'foo'}

But we can't add extra unnamed arguments, if we are using named arguments for some of the required args.
>>> print_argument_info(1, 2, 'hello', 'world', fourth='boo', third='bar', y='baz', foo_level='foo')
Traceback (most recent call last):
 ...
TypeError: print_argument_info() got multiple values for keyword argument 'fourth'

The reason for this is that the supposedly 'extra' unnamed arguments get interpreted as the normal arguments in the argument list,
and the later keyword arguments seem to be duplicate definitions. In other words, YOU CAN'T CALL WITH EXTRA UNNAMED ARGS UNLESS YOU ARE USING ALL THE NORMAL ARGUMENTS. This makes sense, because how would Python know that you want the later unnamed arguments to NOT be interpreted as the next arguments in the argument list?
