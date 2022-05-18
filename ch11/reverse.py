def reverse(code):

    # Base Case
    if len(code) == 1:
        return code[0]

    # Subprogram
    return reverse(code[1:len(code)]) + code[0]


# Unit Test Cases
import unittest


class test_reverse(unittest.TestCase):
    def test_count_x(self):
        self.assertEqual(reverse('abcd'), 'dcba')


if __name__ == '__main__':
    unittest.main()
