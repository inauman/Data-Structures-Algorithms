class TreeNode:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def search(self, search_value, node):
        # Base Case
        if node is None or search_value == node.value:
            return node
        elif search_value < node.value: # traverse the left side
            node = node.leftChild
            return self.search(search_value, node)
        else:  #value > node.value,  traverse the right side
            node = node.rigthChild
            return self.search(search_value, node)
            # Sub problem

    def insert(self, insert_value, node):

        if insert_value < node.value:  #left side of the tree
            if node.leftChild is None:
                node.leftChild = TreeNode(insert_value)
            else:
                node = node.leftChild
                node.insert(insert_value, node)
        elif insert_value > node.value:  # rigth side of the tree
            if node.rightChild is None:
                node.rightChild = TreeNode(insert_value)
            else:
                node = node.rigthChild
                node.insert(insert_value, node)

    def delete(self, value_to_delete,  node):

        # Base Case: Reached bottom of the tree and the node(parent) has no children
        if node is None:
            return None
        elif value_to_delete < node.value:
            node.leftChild = self.delete(value_to_delete, node.leftChild)
            return node
        elif value_to_delete > node.value:
            node.rightChild = self.delete(value_to_delete, node.rightChild)
            return node
        elif value_to_delete == node.value:
            if node.leftChild is None: # only one child (right child) node
                return node.rightChild
            elif node.rightChild is None: # only one child (left child) node
                return node.leftChild
            else: # two child nodes
                node.rightChild = self.lift(node.rightChild, node)
                return node
    
    def lift(self, node, nodeToDelte):
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelte)
            return node
        else:
            nodeToDelte.value = node.value
            return node.rightChild
        
    def __repr__(self):
        pass


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
