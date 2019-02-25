from unittest import TestCase
from ..balanced_brackets_stack import balanced_brackets


class TestBalancedBrackets(TestCase):
    def test_one(self):
        string = '(hello)[world]'
        self.assertTrue(balanced_brackets(string))

    def test_two(self):
        string = '([)]'
        self.assertFalse(balanced_brackets(string))

    def test_three(self):
        string = '[({}{}{})([])]'
        self.assertTrue(balanced_brackets(string))
