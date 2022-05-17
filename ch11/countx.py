

def countx(mystr):

  # Base Case
  if len(mystr) == 0:
    return 0

  # Subprogram
  if mystr[0] == 'x':
    return 1 + countx(mystr[1:len(mystr)])
  else:
    return countx(mystr[1:len(mystr)])

# Unit Test Cases
import unittest
class test_countx(unittest.TestCase):
  def test_count_x(self):
    self.assertEqual(countx('axbxcxd'), 3)
    
if __name__ == '__main__':
  unittest.main()
