class heap:
    
    def __init__(self):
        self.data = []
        
    def root_node(self):
        return self.data[0]
    
    def last_node(self):
        return self.data[-1]
    
    def left_child_index(self, index):
        return (index * 2 + 1) # formula: leftChild index = 2 * parent index + 1
    
    def rigth_child_index(self, index):
        return (index * 2 + 2) # formula: rightChild index = 2 * parent index + 2
    
    def parent_index(index):
        # formula parent index = (child index - 1) // 2 (note: integer division ==> math.floor)
        return (index -1)//2 # note: two slashes "//" are used for integer divison (instead of using math.floor)