>>> def do_something(what):
...     print what
... 
>>> do_something('hello')
hello
>>> do_something  # doctest: +ELLIPSIS
<function do_something at 0x...>
>>> my_new_function = do_something
>>> my_new_function(5)
5
>>> my_new_function  # doctest: +ELLIPSIS
<function do_something at 0x...>
