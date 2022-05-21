def add_until_100(arr):

    # Base Case
    if len(arr) == 0:
        return 0

    # Sub problem

    # fix: store the computation results in the variable for subsequent use
    sum = arr[0] + add_until_100(arr[1:len(arr)])

    if sum > 100:
        return sum - arr[0]
    else:
        return sum


import unittest


class tc_add_sum_arr(unittest.TestCase):
    def test_add_sum_until_100(self):
        self.assertEqual(add_until_100([1, 2, 3, 4]), 10)
        self.assertEqual(add_until_100([1, 2, 300, 4]), 7)


if __name__ == '__main__':
    unittest.main()
