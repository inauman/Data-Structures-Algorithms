class LinkedList:

    # only thing LL does is hold a reference to the head node
    def __init__(self):
        self.head = None

    # return the data of a node for a given index
    def read(self, index):
        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            if current_node is None:
                return 'None'
            current_index += 1
        return current_node.data

    # search for a matching node and return index
    def search(self, search_str):
        # start with the head of the llist
        current_node = self.head
        current_index = 0

        while True:
            if current_node is None:
                return 'None'
            elif current_node.data == search_str:
                return current_index

            current_node = current_node.next
            current_index += 1

    def insert_at_index(self, index, value):
        # start with the head of the llist
        current_node = self.head
        current_index = 0

        # prep the new node
        new_node = Node(value)

        while current_index < index:
            current_node = current_node.next

            if current_node is None:
                break
            current_index += 1

        if current_index == index:
            new_node.next = current_node.next
            current_node.next = new_node
            return 'Done'
        else:
            return 'index out of bound'

    # a simple representation of the LL
    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")

        # join the nodes using -> separator
        return " -> ".join(nodes)


import unittest
from Node import Node


class tc_linkedlist(unittest.TestCase):
    def setUp(self):
        self.first_node = Node('a')
        self.second_node = Node('b')
        self.third_node = Node('c')
        self.fourth_node = Node('d')
        self.fifth_node = Node('e')
        self.first_node.next = self.second_node
        self.second_node.next = self.third_node
        self.third_node.next = self.fourth_node
        self.fourth_node.next = self.fifth_node
        self.llist = LinkedList()
        self.llist.head = self.first_node
        #print(self.llist)

    def tearDown(self):
        #print(self.llist)
        pass

    def test_read_in_ll(self):
        self.assertEqual(self.llist.read(2), 'c')

    def test_read_not_in_ll(self):
        self.assertEqual(self.llist.read(20), 'None')

    def test_search_in_ll(self):
        self.assertEqual(self.llist.search('d'), 3)

    def test_search_not_in_ll(self):
        self.assertEqual(self.llist.search('m'), 'None')

    def test_insert_in_ll(self):
        self.assertEqual(self.llist.insert_at_index(1, 'mayesha'), 'Done')

    def test_insert_out_of_range_in_ll(self):
        self.assertEqual(self.llist.insert_at_index(20, 'aaa'),
                         'index out of bound')


if __name__ == '__main__':
    unittest.main()
'''
from Node import Node
from LinkedList import LinkedList
first_node = Node('a')
second_node = Node('b')
third_node = Node('c')
fourth_node = Node('d')
fifth_node = Node('e')
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
llist = LinkedList()
llist.head = first_node
llist
llist.read(2)
llist.read(20)
llist.search('d')
llist.search('m')
llist.insert_at_index(1, 'aaa')
llist.insert_at_index(10, 'bbb')
'''
