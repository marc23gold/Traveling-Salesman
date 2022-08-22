#Vertex class
class Vertex:
    # Time complexity:  O(1)
    # Space complexity:  O(1)
    # Constructor
    def __init__(self, label):
        self.label = label


    #Time complexity: O(1)
    #Space complexity: O(1)
    # How an instance of the class will be shown when printed
    def __repr__(self):
        return "vertex({self.label})".format(self=self)

#Graph class
class Graph:
    #Time complexity: O(1)
    #Space complexity: O(1)
    #Constructor
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    # Time complexity: O(1)
    # Space complexity: O(1)
    # add a vertex to the graph
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # Time complexity: O(1)
    # Space complexity: O(1)
    # adds a directed edge to the graph
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # Time complexity: O(1)
    # Space complexity: O(1)
    # adds an undirected edge to the graph
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # Time complexity: O(1)
    # Space complexity: O(1)
    # Function for how an instance will be represented when printed
    def __repr__(self):
        return "graph({self.adjacency_list},{self.edge_weights})".format(self=self)
