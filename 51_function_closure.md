>>> def function():
...    print "This version of the function was defined and closed into the outer function."

>>> def outer_function():
...    function()

>>> def function():
...    print "This is the function that was redefined after the outer function was defined."

>>> outer_function()
This is the function that was redefined after the outer function was defined.
