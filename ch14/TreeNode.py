class TreeNode:

    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def search(self, value, node):
        # Base Case
        if node is None or value == node.data:
            return node
        elif value < node.data:
            return self.search(value, node.leftChild)
        else: #value > node.data
            return self.search(value, node.rightChild)
        
            # Sub problem
        
    def __repr__(self):
        return str(self.data)


'''
from TreeNode import TreeNode
leftChild = TreeNode(25)
rightChild = TreeNode(75)
root = TreeNode(50, leftChild, rightChild)
'''
import unittest
class tc_treenode(unittest.TestCase):
    def setUp(self):
        self.leftChild = TreeNode(25)
        self.rightChild = TreeNode(75)
        self.tree = TreeNode(50, self.leftChild, self.rightChild)
        print(self.tree)

    def tearDown(self):
        #print(self.llist)
        pass

    def test_search_in_tree(self):
        self.assertEqual(self.tree.search(75, self.tree).data, 75)

if __name__ == '__main__':
    unittest.main()