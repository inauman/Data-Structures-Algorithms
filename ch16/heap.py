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
