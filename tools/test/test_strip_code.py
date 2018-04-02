import unittest

from tools.strip_code import clean_line


class TestCleanLine(unittest.TestCase):
    def test_blank_line(self):
        self.assertEqual(clean_line("\n"), "\n")
