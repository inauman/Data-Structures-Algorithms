def sum(arr):
    #Base Case
    if len(arr) == 1:
        return arr[0]

    # Subproblem
    return arr[0] + sum(arr[1:len(arr)])


# Unit Test Cases
import unittest


class test_array_sum(unittest.TestCase):
    def test_sum_array(self):
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)

if __name__ == '__main__':
    unittest.main()
