def double_array(arr, index=0):

    # Base Case
    if index >= len(arr):
        return

    # Subprogram
    arr[index] *= 2
    double_array(arr, index + 1)
    return arr

#print(double_array([1, 2, 3, 4, 5]))

import unittest


class test_doublearray(unittest.TestCase):
    def test_double_array(self):
        self.assertEqual(double_array([1, 2, 3, 4, 5]), [2, 4, 6, 8, 10])


if __name__ == "__main__":
    unittest.main()

    