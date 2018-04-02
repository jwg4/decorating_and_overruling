import unittest

from tools.strip_code import clean_line


class TestCleanLine(unittest.TestCase):
    def test_blank_line(self):
        self.assertEqual(clean_line("\n"), "\n")

    def test_code_line(self):
        line = ">>> j = partial(f, 7, 7)\n"
        self.assertEqual(clean_line(line), line)