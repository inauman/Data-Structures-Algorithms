# Weighted Graph Vertex

import unittest


class wgvertex:

    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}

    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight

    def __repr__(self) -> str:

        result = []
        for vertex in self.adjacent_vertices:
            edge_wt = f'{vertex.value}: {self.adjacent_vertices[vertex]}'
            result.append(edge_wt)
        return f'{self.value} --> {result}'


class tc_graph(unittest.TestCase):

    def setUp(self):
        self.dallas = wgvertex('Dallas')
        self.toronto = wgvertex('Toronto')
        self.phoenix = wgvertex('Phoenix')
        self.dallas.add_adjacent_vertex(self.toronto, 138)
        self.dallas.add_adjacent_vertex(self.phoenix, 1100)
        self.phoenix.add_adjacent_vertex(self.dallas, 1065)
        self.toronto.add_adjacent_vertex(self.dallas, 216)

    def tearDown(self):
        pass

    def test_wgtree(self):
        print(self.dallas)
        # print(self.dallas.adjacent_vertices)


if __name__ == '__main__':
    unittest.main()
