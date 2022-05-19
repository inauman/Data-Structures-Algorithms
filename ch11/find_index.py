#s = 'abcdefghijklmnopqrstuvwxyz'


def find_index_of_x(s, index=0):

    if s[0] == 'x':
        return index
    else:
        return find_index_of_x(s[1:], index + 1)


import unittest


class tc_find_index(unittest.TestCase):
    def test_find_index_of_x(self):
        self.assertEqual(find_index_of_x('abcdefghijklmnopqrstuvwxyz'), 23)
        self.assertEqual(find_index_of_x('abxcdefghijklmnopqrstuvwxyz'), 2)


if __name__ == '__main__':
    unittest.main()
