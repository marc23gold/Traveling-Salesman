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

print(ok)

print(g.adjacency_list)

g.add_undirected_edge(vertex[0], vertex[1],float(ok[0][4]))
g.add_und

print(g.adjacency_list)



#add the edges
"""def add_edges():
    # outer loop accessing the rows
    for x in range(len(ok)):
        #inner loop accessing the columns
        for y in ok[x][x+2]:
            if y == 0:
                break
            g.add_undirected_edge(vertex[0], vertex[1], int(ok[1][x+2]))
            if y == '':
                break"""

#print(g.adjacency_list)



