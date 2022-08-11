import csv
from readcsv import *
from graph import *

ok = loadDistance('distance_table.csv')

vertex = []
for x in range(27):
    vertex.append(Vertex(x))

#initialized an instance of the graph class
g = Graph()

#added the vertex
for x in range(27):
    g.add_vertex(vertex[x])

#print(ok) test

#print(g.adjacency_list)
#O(N^2)
def create_graph():
    for x in range(len(ok)):
        for y in range(len(ok)):
            right = g.add_undirected_edge(vertex[x], vertex[y],float(ok[x][y]))
    return right
#note to self: you're going to call the edge weights using the vertex indicies like shown below 
create_graph()
#print(g.adjacency_list)
#print(g.edge_weights)
#print(g.adjacency_list[vertex[0]])
#print(g.edge_weights[(vertex[2], vertex[4])])




























