import csv
from readcsv import *
from graph import *

ok = loadDistance()

vertex = []
for x in range(27):
    vertex.append(Vertex(x))

#initialized an instance of the graph class
g = Graph()

#added the vertex
for x in range (len(ok)):
    g.add_vertex(vertex[x])

print(ok)



#add the edges
"""def add_edges():
    for x in range(len(ok)):
        for y in ok[x][x+2]:
             g.add_undirected_edge(vertex[0], vertex[], weight = ok[][] )
        if x == '':
            break"""




