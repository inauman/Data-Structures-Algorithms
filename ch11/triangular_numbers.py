# Triangular Number series
# 1, 3, 6, 10, 15, 21, 28
# TN (Triangular Number) = N + TN(N-1)

def triangular_number(n):

    # Base Case
    if n == 1:
        return 1

    tn = n + triangular_number(n - 1)

    return tn


# Unit Test Cases
import unittest


class test_triangular_numbers(unittest.TestCase):
    def test_triangular_number(self):
        self.assertEqual(triangular_number(7), 28)


if __name__ == '__main__':
    unittest.main()
