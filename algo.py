from distances import *
from package import *
from readcsv import *
from truck import *

addressList = loadAddresses('address.csv')
#there are 27 addresses being put into the list
#print(len(addressList))
#print(addressList)

#dictionary that will have index as the key and address as the thing
vertexToAddressDictionary = {}

#assigns a key with value of integer zero to equal HUB
vertexToAddressDictionary[0] = addressList[0][1]
for x in range(1,27):
        vertexToAddressDictionary[x] = addressList[x][1]

addressToVertexDictionary = {}
addressToVertexDictionary[addressList[0][1]] = 0
for x in range(27):
        addressToVertexDictionary[addressList[x][1]] = x
#print(addressToVertexDictionary)


package = packHash.search(20)
packageString = package.address
print(addressToVertexDictionary[packageString])

#print(vertexToAddressDictionary)
#key_list = list(vertexToAddressDictionary)
#val_list = list()

def algo (truck):
        newarray = []
        #i is the index of the list packages x is the package item
        #so for package items in truck.packages pass through the list of packages
        for i,x in enumerate(truck.packages):
                #this is getting the package values from the packHash hashtable using passing in the value x from the package list from the truck
                package = packHash.search(x)
                #getting the address string from the package object
                packageString = package.address
                #converts the packageString into an index the getDistance function will understand
                vertexId2 = addressToVertexDictionary[packageString]
                #setting the initial from value to the HUB will be found
                if i == 0:
                        #assigning the from value to be HUB
                        vertexId1 = addressToVertexDictionary['HUB']
                        min = 1000
                        #
                        for y in range(len(truck.packages)):

                                dist = getDistance(vertexId1, vertexId2)
                                if dist < min:
                                        min = dist
                                        nextFromVertex = vertexId2
                                        address = vertexToAddressDictionary[vertexId2]
                                        newarray.append(address)
                        return newarray

                else:
                         min = 1000
                         #
                         for y in range(len(truck.packages)):

                                 dist = getDistance(newarray[i-1], vertexId2)
                                 if dist < min:
                                         min = dist
                                         nextFromVertex = vertexId2
                                         address = vertexToAddressDictionary[vertexId2]
                                         newarray.append(address)
                #         #sets the from value to the previous address
                #         vertexId1 = truck.packages[i-1]
                # distance = getDistance(vertexId1, vertexId2)
                # newarray.append(distance)

print(algo(truck1))














# #vectorToAddressDictionary = {
#     # 0: 'HUB',
#     # 1:
#     # 2: '1330 2100 S'
#     # 3:
#     # 4:
#     # 5: '195 W Oakland Ave',
#     # 6:
#     # 7:
#     # 8: '233 Canyon Rd'
#     # 9: '2530 S 500 E'
#     # 10:
#     # 11:
#     # 12:
#     # 13: '3060 Lester St'
#     # 14:
#     # 15:
#     # 16:
#     # 17:
#     # 18: '380 W 2880 S'
#     # 19: '410 S State St'
#     # 20:
#     # 21:
#     # 22:
#     # 23:
#     # 24:
#     # 25:
#     # 26:
# #}
# r = packHash.search(9)
# rrr = r.address
# print(rrr)
#
# print(vertexToAddressDictionary[3])
#
# def algo(truck) :
#     #this is the start address that will be passed into the getDistance function
#     startingAddress = 'HUB' or 0
#     #creating new list for sorted passed in list from truck.packages to be stored
#     newlist = []
#     for x in truck.packages:
#         newlist.append()
#         #for every package id that is searched from the list of the current truck.package list
#         #it will be stored into the variable package so that it can be used later
#         package = packHash.search(x)
#         #this is getting the name of the address of the package being stored in the variable packageString
#         packageString = package.address
#         """next line takes the package string and gets the vector index using some dictionary method"""
#         """the vector index is used as the represenation of the address"""
#         """next line takes the vector index and passes it into a block of code or function that gets the next package with the min distance"""
#         """next line puts that package into the truck.package list"""
#         "return truck.package list"
#         "done"
#         #gets information from package with current package
#         packInfo = packHash.search(x)
#         #I need to get the package address
#         #if #current package
#         return # new truck package list
#
#
#
#
#
# #I know need to create a dictionary that corresponds the address with a number