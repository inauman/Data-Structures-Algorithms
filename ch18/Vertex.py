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
        visited_vertices[vertex.value] = True

        # process the visited node, here we are just printing
        print(vertex)

        for adjacent_vertex in vertex.adjacent_vertices:
            if visited_vertices.get(adjacent_vertex.value):
                continue

            self.dfs_traverse(adjacent_vertex, visited_vertices)

    def dfs_search(self, vertex, search_value, visited_vertices={}):
        print(vertex.adjacent_vertices)
        # Return the vertex if it matches with what we are searching for
        if vertex.value == search_value:
            return vertex

         # mark vertex visited by adding it to the hash table
        visited_vertices[vertex.value] = True

        for adjacent_vertex in vertex.adjacent_vertices:
            # Continue if the node has already been visited
            if visited_vertices.get(adjacent_vertex.value):
                continue

            # Return the adjacent_vertex if it matches with what we are searching for
            if adjacent_vertex.value == search_value:
                return adjacent_vertex

            # Didn't find the vertex yet? ok, keep calling the search function recursively
            vertex_searching_for = self.dfs_search(
                adjacent_vertex, search_value, visited_vertices)

            # Important: This code is a combination of loop and recursion. Within the graph, there are many loops and each loop needs to go through recursion. So, break from a loop only if we found a value. Otherwise, if we didn't find the value, LOOP will continue to move forward with the remaining loops in the graph.
            if vertex_searching_for:
                return vertex_searching_for

        # return none if we can't find the node in the tree

        return None

    def bfs_traverse(vertex):

        # queue will be used to power up the bfs FIFO traversal
        # while queue can be implemented in different ways, will be using simple list here
        queue = []

        visited_vertices = {}

        visited_vertices[vertex.value] = True
        queue.append(vertex)
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex.value)

            for adjacent_vertex in current_vertex.adjacent_vertices:
                if not visited_vertices.get(adjacent_vertex.value):
                    visited_vertices[adjacent_vertex.value] = True

                    queue.append(adjacent_vertex)


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
        self.helen.add_adjacent_vertex(self.candy)
        self.derek.add_adjacent_vertex(self.elaine)
        self.derek.add_adjacent_vertex(self.gina)
        self.gina.add_adjacent_vertex(self.irena)

    def tearDown(self):
        pass
    '''
    def test_dfs_traverse(self):
        self.alice.dfs_traverse(self.alice)

    
    def test_dfs_search(self):
        self.alice.dfs_search(self.alice, "Derek").value'''

    def test_bfs_traverse(self):
        self.alice.bfs_traverse()


if __name__ == '__main__':
    unittest.main()
