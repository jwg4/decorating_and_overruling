>>> a = [1, 2, 4]
>>> b = a
>>> b
[1, 2, 4]
>>> b.append(5)
>>> b
[1, 2, 4, 5]
>>> a
[1, 2, 4, 5]

>>> a = 'Hello'
>>> b = a
>>> b
'Hello'
>>> b.append(' World')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
>>> b = 'hello'
>>> a
'Hello'
>>> b
'hello'

>>> a = ['foo', 'bar', 'baz']
>>> b = a
>>> b
['foo', 'bar', 'baz']
>>> b = [5, 4, 3, 2, 1]
>>> a
['foo', 'bar', 'baz']
>>> b
[5, 4, 3, 2, 1]
