def test_munge(a, **kwargs):
    return "foo %s bar %s baz" % (a, kwargs)

def trial_decorator(f):
    return f

