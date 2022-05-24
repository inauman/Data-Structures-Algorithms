class Node:

    # create the node with 1) data and 2) placeholder to reference the next node
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # a simple node representation 
    def __repr__(self):
        return self.data
