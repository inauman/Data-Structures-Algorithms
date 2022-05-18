def char_counter(arr):
    # Base Case
    if len(arr) == 0:
        return 0
        
    # Subprogram
    char_count = len(arr[0]) + char_counter(arr[1:])
    return char_count

# Unit Tests
import unittest

class test_char_counter(unittest.TestCase):
    def test_char_count(self):
        self.assertEqual(char_counter(['ab','c','def','ghij']), 10)

if __name__ == '__main__':
    unittest.main()
