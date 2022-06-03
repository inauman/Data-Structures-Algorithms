# Vertex == Node
class Vertex:

    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    '''def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)'''
    
    # undirected graph i.e. if adding "alice -> bob", automatically add "bob -> alice"
    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)
        
        
