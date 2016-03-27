The next few files in the sequence are all about solving the following problem:

We have a Python function which looks a bit like this:
```
def orig_fun(x):
    # do something
    
    # do some more stuff
    y = transformation(x)
    
    return external_fun(y)
```

Here `external_fun` is a function we can't change from another module. We would like to write a decorator which transforms `orig_fun` to be something like this:

```
def new_version_of_orig_fun(x):
    # do something
    
    # do some more stuff
    y = transformation(x)
    
    z = additional_transformation(y, x)
    
    return external_fun(y, z=z)
```

If it wasn't for the return value, which needs to call the same function in each case, eg. if we had

```
def orig_fun_wo_return_fun(x):
    # ...

    return dict(y=y)
```
and we wanted to have 

```
def new_version_wo_return_fun(x):
    # ...
    
    return dict(y=y, z=z)
```

it would be very easy - we could just take the return value in the decorator, add the term `z=z`, and return it in the decorated function.

However, in our case, we can't assume that we can extract `y` from `external_fun(y)`. This repo is for trying some other things to see if we can get it to work.
