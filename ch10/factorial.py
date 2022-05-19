def factorial(n):
    # Base Case
    if n == 1:
        return 1
    else:
        #Subprogram
        factn = n * factorial(n - 1)
        return factn


import unittest


class testfactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)


if __name__ == '__main__':
    unittest.main()
