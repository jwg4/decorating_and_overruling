>>> import my_module

>>> def outer_function():
...     my_module.my_function()

>>> def my_function():
...     print "This is the function that was redefined after the outer function was defined."

>>> my_module.my_function = my_function

>>> outer_function()
This is the function that was redefined after the outer function was defined.
