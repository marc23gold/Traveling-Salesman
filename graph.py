#vertex
class Vertex:
    #O(1)
    def __init__(self, label):
        self.label = label
    #O(1)
    def __repr__(self):
        return "vertex({self.label})".format(self=self)

class Graph:
    #O(1)
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    #O(1)
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    #O(1)
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    #O(1)
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    #O(1)
    def __repr__(self):
        return "graph({self.adjacency_list},{self.edge_weights})".format(self=self)
