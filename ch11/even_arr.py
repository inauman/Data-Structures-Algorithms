'''
This is just one possible implementation using recursion & iteration...it can be implemented using more simpler approach but recursion + iteration is more fun :)
'''
def even_array(arr):

    # Base Case
    if len(arr) == 1:
        return arr[0:1]
            
    # Subproblem
    array_numbers = arr[0:1] + even_array(arr[1:])

    # Collector array for holding even numbers
    even_numbers = []

    # Iterate through the array of numbers
    for number in array_numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    
    return even_numbers
    
# Unit Test Cases
import unittest


class test_reverse(unittest.TestCase):
    def test_even_array(self):
        self.assertEqual(even_array([1,3,4,6,8,9,11]), [4,6,8])

if __name__ == '__main__':
    unittest.main()
