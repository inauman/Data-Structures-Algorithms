# Vertex == Node
import unittest


class vertex:

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

    def __repr__(self):
        return self.value

    # DFS: Depth-First Search is based on recursion i.e. it uses STACK (LIFO) as an engine to drive the search forward. With this approach traversal drifts away from the starting node, move as far as possible, and comeback. BFS (Breadth-First Search) on the other hand is powered by QUEUE (FIFO) where the travesal completes for all the neighbors of the starting node and then it ripples to wider network of nodes.

    def dfs_traverse(self, vertex, visited_vertices={}):

        # mark vertex visited by adding it to the hash table
        visited_vertices[vertex.value] = "True"

        # process the visited node, here we are just printing
        print(vertex)

        for adjacent_vertex in vertex.adjacent_vertices:
            if visited_vertices.get(adjacent_vertex.value):
                continue

            self.dfs_traverse(adjacent_vertex, visited_vertices)


class tc_graph(unittest.TestCase):

    def setUp(self):
        self.alice = vertex('Alice')
        self.bob = vertex('Bob')
        self.candy = vertex('Candy')
        self.derek = vertex('Derek')
        self.fred = vertex('Fred')
        self.helen = vertex('Helen')
        self.gina = vertex('Gina')
        self.irena = vertex('Irena')
        self.elaine = vertex('Elaine')

        self.alice.add_adjacent_vertex(self.bob)
        self.alice.add_adjacent_vertex(self.candy)
        self.alice.add_adjacent_vertex(self.derek)
        self.alice.add_adjacent_vertex(self.elaine)
        self.bob.add_adjacent_vertex(self.fred)
        self.fred.add_adjacent_vertex(self.helen)
        self.derek.add_adjacent_vertex(self.elaine)
        self.derek.add_adjacent_vertex(self.gina)
        self.gina.add_adjacent_vertex(self.irena)

    def tearDown(self):
        pass

    def test_dfs(self):
        self.alice.dfs_traverse(self.alice)


if __name__ == '__main__':
    unittest.main()
