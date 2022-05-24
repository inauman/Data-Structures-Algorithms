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

'''