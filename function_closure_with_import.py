from my_module import my_function

def outer_function():
    my_function()

def my_function():
    print "This is the function that was redefined after the outer function was defined."

outer_function()

