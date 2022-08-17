#importing csv, read csv file, and the graph class
import csv
from readcsv import *
from graph import *

"""calling the loadDistance function from readcsv with the argument distance_table
and assigning the return value to the ok variable. This will get the two dimensional array
that will make the adjacency matrix"""
distances = loadDistance('distance_table.csv')

addressok = loadAddresses('address1.csv')

#O(N)
#gets the address index
def addressIndex(address):
    #searches through the number of rows in addressok
    for i,x in enumerate(addressok):
        # print(address, x[1])
        #if the address string that is being passed in is in the second column of the x row return the index of the x row
        if address in x[1]:
            return i
    print(address)

#O(N)
def getDistanceTo(address1, address2):
    #return the the float of the index of distance
    return float(distances[addressIndex(address1)][addressIndex(address2)])

vertex = []
def vertexInGraph():
    "making an array that will contain the vertexes of the graph "

    """for loop that will create and add an instance of the Vertex class at each index
    in the array resulting in 27 vertexes that will be called using vertex[x] """
    #O(N)
    for x in range(len(distances)):
        d = vertex.append(Vertex(x))
    return  d

vertexInGraph()

#initialized an instance of the graph class
g = Graph()

#O(N)
#added the vertex to the graph class
for x in range(len(distances)):
    g.add_vertex(vertex[x])




#O(N^2)
def create_graph():
    for x in range(len(distances)):
        for y in range(len(distances)):
            graph = g.add_undirected_edge(vertex[x], vertex[y],float(distances[x][y]))
    return graph
#note to self: you're going to call the edge weights using the vertex indicies like shown below
create_graph()

#functions to test code
def test(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    print(g.adjacency_list[vertex[a]])
    print(g.edge_weights[(vertex[b], vertex[c])])


#functions to test code
def test2():
    print(g.adjacency_list)
    print(g.edge_weights)

#test(5,18,2)













