def sum(arr):
    #Base Case
    if len(arr) == 1:
        return arr[0]

    # Subproblem
    return arr[0] + sum(arr[1:len(arr)])


# Unit Test Cases
import unittest


class test_countx(unittest.TestCase):
    def test_count_x(self):
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)


if __name__ == '__main__':
    unittest.main()
