'''
Fibonacci sequence
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''


#n starts at 0, n=10 means, 11th number in the Fib series
def fib_v1(n):

    # Base Case
    if n == 0 or n == 1:
        return n
    # Sub problem
    return fib_v1(n - 1) + fib_v1(n - 2)


print(fib_v1(10))


#n starts at 0, n=10 means, 11th number in the Fib series
def fib_v2(n, memo={}):

    # Base Case
    if n == 0 or n == 1:
        return n

    # Sub problem
    # Use Memoization i.e. store the computation results in varaibles for subsequent use

    # check if the key i.e. computation result exist in the hash table (dictionary). If not, store them in the hash table
    # Also, pass the hash table in the stack for the parent functions to use the data from the child recursive calls
    if not memo.get(n):
        memo[n] = fib_v2(n - 1, memo) + fib_v2(n - 2, memo)

    return memo[n]


print(fib_v2(10))

import unittest
from datetime import datetime


class tc_fib_sequence(unittest.TestCase):
    def test_fib_v1(self):
        start_time = datetime.now()
        self.assertEqual(fib_v1(10), 55)
        end_time = datetime.now()
        print(f'Duration (v1) --> {end_time - start_time}')

    def test_fib_v2(self):
        start_time = datetime.now()
        self.assertEqual(fib_v2(10), 55)
        end_time = datetime.now()
        print(f'\nDuration (v2) --> {end_time - start_time}')


if __name__ == '__main__':
    unittest.main()
