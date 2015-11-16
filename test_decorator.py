import unittest

from decorator import trial_decorator as decorator
from decorator import test_munge as munge

def transform(x):
    return sorted(x)

class TestDecorator(unittest.TestCase):
    def setUp(self):
        def fn(x):
            y = transform(x)
            return munge(y)

        self.function = fn

    def test_decorator_works(self):
        decorated = decorator(self.function)
        x = "asdfasdf"
        z = dict(w="wozzat", k="keyber")
        expected = munge(transform(x), z=z)
        self.assertEqual(decorated(x), expected)

