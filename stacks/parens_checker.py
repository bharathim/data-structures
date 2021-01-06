from stack import Stack
import unittest


def is_balanced(input_str: str) -> bool:
    """Check whether a given input string has balanced parenthesis and brackets

    :type input_str: str
    :rtype: bool
    """
    open_paren = tuple("{[(")
    closed_paren = tuple("}])")
    paren_map = dict(zip(closed_paren, open_paren))
    s = Stack()

    balanced = False
    for c in input_str:
        if c in open_paren:
            s.push(c)
        elif c in closed_paren:
            if s.is_empty():
                return False
            elif paren_map[c] == s.pop():
                balanced = True

    return balanced and s.is_empty()


class TestBalancedParenthesisChecker(unittest.TestCase):

    def test_is_empty(self):
        self.assertFalse(is_balanced(""))

    def test_is_non_paren(self):
        self.assertFalse(is_balanced("0"))

    def test_is_only_open_paren(self):
        self.assertFalse(is_balanced("["))

    def test_is_only_close_paren(self):
        self.assertFalse(is_balanced("]"))

    def test_is_balanced_true(self):
        self.assertTrue(is_balanced("[]"))

    def test_is_balanced_starting_closing_paren(self):
        self.assertFalse(is_balanced("]()"))

    def test_is_balanced_multiple(self):
        self.assertTrue(is_balanced("[(){}]"))


if __name__ == '__main__':
    unittest.main()
