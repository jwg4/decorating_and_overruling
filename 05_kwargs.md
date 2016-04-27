** works like * but for named arguments.

When you define a function, ** means to take all the named arguments which weren't matched, and put them into a dict.
>>> def do_something_with_a_dict(**kwargs):
...     print len(kwargs)
...     print kwargs.__class__
...     for k in kwargs:
...         print k, kwargs[k]

>>> do_something_with_a_dict(a=1, b=2)
2
<type 'dict'>
a 1
b 2

(kwargs is just the common name used for the dictionary argument. Any name can be used.)

When you call a function, ** means to take a dict, and expand it into individual named variables.
>>> def what_they_ate(mummy, daddy, baby):
...     print "Mummy bear's porridge was too %s." % mummy
...     print "Daddy bear's porridge was too %s." % daddy
...     print "Baby bear's porridge was just %s." % baby

>>> d = {'daddy': 'cold', 'mummy': 'hot', 'baby': 'right'}
>>> what_they_ate(**d)
Mummy bear's porridge was too hot.
Daddy bear's porridge was too cold.
Baby bear's porridge was just right.
