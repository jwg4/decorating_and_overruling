We can write all arguments in order without naming them, including at least as many as all non-optional arguments, and at most as many as all arguments.

>>> def this_little_pig_went_to(market, home, roast_beef=None):
...     print 'This little pig went to %s' % market
...     print 'This little pig stayed at %s' % home
...     print 'This little pig had %s' % roast_beef

>>> this_little_pig_went_to('East Ham', 'school')
This little pig went to East Ham
This little pig stayed at school
This little pig had None

>>> this_little_pig_went_to('East Ham', 'school', 'swine flu')
This little pig went to East Ham
This little pig stayed at school
This little pig had swine flu

This includes the situation where all arguments are optional:
>>> def product_of_up_to_five_numbers(a=1, b=1, c=1, d=1, e=1):
...     return a * b * c * d * e

>>> product_of_up_to_five_numbers()
1

>>> product_of_up_to_five_numbers(4)
4

>>> product_of_up_to_five_numbers(2, 2, 2, 2)
16

>>> product_of_up_to_five_numbers(2, 3, 5, 7, 11)
2310

If all arguments are optional. we could include any subset we choose, in any order we choose, by passing them with names:
>>> product_of_up_to_five_numbers(d=21, b=33)
693

>>> product_of_up_to_five_numbers(e=11, d=13, c=7, a=3, b=41)
123123

To combine unnamed and named arguments, we have to put the named arguments first
>>> product_of_up_to_five_numbers(1, 2, d=3)
6

>>> product_of_up_to_five_numbers(d=10, 1, 2)
Traceback (most recent call last):
...
SyntaxError: non-keyword arg after keyword arg

>>> product_of_up_to_five_numbers(7, 7, 7, b=7, 7)
Traceback (most recent call last):
...
SyntaxError: non-keyword arg after keyword arg

This applies even if we put a named argument first, and it actually refers to the first argument:
>>> product_of_up_to_five_numbers(a=10, 12)
Traceback (most recent call last):
...
SyntaxError: non-keyword arg after keyword arg
