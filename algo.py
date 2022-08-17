from distances import *
from package import *
from readcsv import *


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
#print(addressToVertexDictionary[packageString])

#print(vertexToAddressDictionary)
#key_list = list(vertexToAddressDictionary)
#val_list = list()

def algo (truck):
        #this array will hold the sorted address values that will later be turned back into the package number
        newarray = []
        nextToAddress = truck.address
        #i is the index of the list packages x is the package item
        #so for package items in truck.packages pass through the list of packages
        for i,x in enumerate(truck.packages):


                        #setting the minimum value to be a large number
                        min = 1000
                        nextFromAddress = None
                        nextBestAddress = None
                        #loop that passes through the truck array till a minimum value is found
                        for packages in truck.packages:
                                """calling the getDistance in truck to get the distance between the two vertexes and
                                #assigning it to dist"""
                                if packages in newarray:
                                        continue

                                package = packHash.search(packages)


                                dist = getDistanceTo(nextToAddress, package.address)
                                """if the variable dist is less than the minimum which will be continously reassigned to 
                                the lowest value distance value found in the list then assign the vertexID from the dist
                                to outside dist"""
                                n = sum([1 for p in truck.packages if packHash.search(p).deadline != "EOD" and p not in newarray])
                                if n and package.deadline == "EOD":
                                    continue
                                if dist < min :
                                        min = dist
                                        nextFromAddress = packages
                                        nextBestAddress = package.address

                        newarray.append(nextFromAddress)
                        nextToAddress = nextBestAddress
        return newarray


                # else:
                #         min = 1000
                #          findsecondmin = []
                #          for packages in range(len(truck.packages)):
                #                 dist = getDistance(nextFromVertex, vertexId2)
                #                 #if dist == 0 or 0.0:
                #                         # #find the second minimum value
                #                         # # this adjacencyMatrix will be used to get the second min value
                #                         # adjacencyMatrix = loadDistance('distance_table.csv')
                #                         # for row in adjacencyMatrix:
                #                         #         row.sort()
                #                         # #print(len(adjacencyMatrix))
                #                         # #print(adjacencyMatrix)
                #                         # secondMinString = adjacencyMatrix[vertexId2][1]
                #                         #
                #                         # min = float(secondMinString)
                #                         # nextFromVertex = vertexId2
                #                         # address = vertexToAddressDictionary[nextFromVertex]
                #                         # newarray.append([address, min])
                #                         # return newarray
                #                 #         # min = dist
                #                 #          # findsecondmin.append(min)
                #                 #         currentIndex = i
                #                 #         nextIndex = currentIndex + 1
                #                 #         nextFromVertex = truck.packages[nextIndex]
                #                 #         address = vertexToAddressDictionary[vertexId2]
                #                 #         newarray.append(address)
                #                 #          #try just moving to the next item in the list
                #
                #                 if dist < min:
                #                         min = dist
                #                         nextFromVertex = vertexId2
                #                         address = vertexToAddressDictionary[nextFromVertex]
                #         newarray.append([address, min])
                #         return newarray
                # #         #sets the from value to the previous address
                # #         vertexId1 = truck.packages[i-1]
                # # distance = getDistance(vertexId1, vertexId2)
                # # newarray.append(distance)





#finding the second minimum value for the newly sorted list

#this gets the index of the secnd mimum value to pass to the vertex
#adjacencyMatrix2 = loadDistance('distance_table.csv')
#econdMinIndex = adjacencyMatrix2.index()






















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