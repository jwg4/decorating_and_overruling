Functions have a name, and the name is set at the time of defining the function.
>>> def hello(person):
...     print "Hello %s" % person

>>> hello  # doctest: +ELLIPSIS
<function hello at 0x...>

If we assign this function to another variable, it still keeps its original name.
>>> greet = hello

>>> greet("Sophie")
Hello Sophie

>>> greet  # doctest: +ELLIPSIS
<function hello at 0x...>

However, we can change the name
>>> greet.__name__ = "my_fn"

>>> greet  # doctest: +ELLIPSIS
<function my_fn at 0x...>

Because there is really only one function, and two variables which point to it, the original function changes name too.
>>> hello  # doctest: +ELLIPSIS
<function my_fn at 0x...>
