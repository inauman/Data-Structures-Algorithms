class heap:

    def __init__(self):
        self.data = []

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def left_child_index(self, index):
        # formula: leftChild index = 2 * parent index + 1
        return (index * 2 + 1)

    def rigth_child_index(self, index):
        # formula: rightChild index = 2 * parent index + 2
        return (index * 2 + 2)

    def parent_index(index):
        # formula parent index = (child index - 1) // 2 (note: integer division ==> math.floor)
        # note: two slashes "//" are used for integer divison (instead of using math.floor)
        return (index - 1)//2

    def insert(self, value):
        # insert the value at the end of the array
        self.data.append(value)

        # track the index of the newly inserted node
        new_node_index = len(self.data) - 1

        # trickle up the value to be compliant with the heap rule i.e. parent should be more than the child nodes
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            # swap the node
            self.data[self.parent_index(
                new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]

            # update the index of the new node
            new_node_index = self.parent_index(new_node_index)

    def delete(self):
        # only delete the root node from the heap
        # replace is with "the last node"
        # and follow the "trickle down" algorithm

        # delete the root by replacing it with the last node
        self.data[0] = self.data[-1]

        # track the current index of the trickle node
        trickle_node_index = 0

        # trickle down algorith
        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(
                trickle_node_index)

            self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]

            trickle_node_index = larger_child_index

    def has_greater_child(self, index):

        value_parent = self.data[index]
        value_left_child = self.data[self.left_child_index(index)]
        value_right_child = self.data[self.right_child_index(index)]

        return (value_left_child and value_left_child > value_parent) or (value_right_child and value_right_child > value_parent)

    def calculate_larger_child_index(self, index):

        value_parent = self.data[index]
        value_left_child = self.data[self.left_child_index(index)]
        value_right_child = self.data[self.right_child_index(index)]

        # if there is no right child
        if not value_right_child:
            return self.left_child_index(index)

        # if right child > left child
        if value_right_child > value_left_child:
            return self.rigth_child_index(index)
        else:
            return value_left_child(index)
