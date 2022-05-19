def staircase_paths(steps):

    # Base Case
    if steps < 0:
        return 0
    if steps in (0, 1): # While steps 0 should ideally be zero, this is a clever trick to eliminate hardcoding all the base cases (steps 2 & 3)
        return 1
    '''    
    We don't need to hardcode the following base cases due to the above trick of leveraging the above trick utilizing modified zero base case
    if steps == 2:
            return 2
        if steps == 3:
            return 4
    '''
    
    # Sub-problem
    
    return staircase_paths(steps - 1) + staircase_paths(steps - 2) + staircase_paths(steps - 3)

print(staircase_paths(5))

import unittest

class tc_staircase_paths(unittest.TestCase):

    def test_staircase_paths(self):
        self.assertEqual(staircase_paths(5), 13)
        self.assertEqual(staircase_paths(3), 4)

if __name__ == '__main__':
    unittest.main()