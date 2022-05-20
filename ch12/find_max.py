'''
First version time complexity is O(2^N) as it is simply using recursion without storing the computation results
Time Complexity: O(2^N)
'''
def find_max_v1(arr):
    if len(arr) == 1:
        return arr[0]

    if arr[0] > find_max_v1(arr[1:len(arr)]):
        return arr[0]
    else:
        return find_max_v1(arr[1:len(arr)])

'''
This second version is using dynamic programming technique of memoization where the computation results are stored for subsequent use and hence reducing the number of recursive calls.
Time Complexity: O(N)
'''
def find_max_v2(arr):
    if len(arr) == 1:
        return arr[0]

    max_result = find_max_v2(arr[1:len(arr)])
    if arr[0] > max_result:
        return arr[0]
    else:
        return max_result

import unittest
from datetime import datetime
class tc_find_max(unittest.TestCase):
    def test_find_max_v1(self):
        start_time = datetime.now()
        self.assertEqual(find_max_v1([1,2,3,4,5]), 5)
        end_time = datetime.now()
        print(f'Duration (v1) --> {end_time - start_time}')
        
    def test_find_max_v2(self):
        start_time = datetime.now()
        self.assertEqual(find_max_v2([1,2,3,4,5]), 5)
        end_time = datetime.now()
        print(f'\nDuration (v2) --> {end_time - start_time}')

if __name__ == '__main__':
    unittest.main()