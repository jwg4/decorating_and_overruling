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
