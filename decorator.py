def test_munge(a, **kwargs):
    return "foo %s bar %s baz" % (a, kwargs)

def trial_decorator(f):
    def g(x):
        global munge
        old_munge = munge
        munge = dict

        old_ret = f(x)
        z = dict(w="wozzat", k="keyber")
        return old_munge(old_ret, **z)
    return g

