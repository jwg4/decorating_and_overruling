
    >>> def print_a_thing(x=None):
    ...     def inner():
    ...         print x
    ...     return inner
    ... 
    >>> def print_a_thing_with_a_default(x=None):
    ...     def inner():
    ...         if x is None:
    ...             x = 1
    ...         print x
    ...     return inner
    ... 
    >>> print_a_thing()()
    None
    >>> print_a_thing(5)()
    5
    >>> print_a_thing_with_a_default()()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 3, in inner
    UnboundLocalError: local variable 'x' referenced before assignment
