import unittest

from tools.strip_code import clean_line


class TestCleanLine(unittest.TestCase):
    def test_blank_line(self):
        self.assertEqual(clean_line("\n"), "\n")

    def test_code_line(self):
        line = ">>> j = partial(f, 7, 7)\n"
        expected = "j = partial(f, 7, 7)\n"
        self.assertEqual(clean_line(line), expected)

    def test_continuation_line(self):
        line = "...     return -1.0 / x\n"
        expected = "    return -1.0 / x\n"
        self.assertEqual(clean_line(line), expected)

    def test_text_line(self):
        line = "We could use partial on a function which doesn't have any arguments, although it doesnt seem very useful:\n"
        self.assertIsNone(clean_line(line))
