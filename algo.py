from distances import *
from package import *
from readcsv import *


addressList = loadAddresses('address.csv')

#dictionary that will have index as the key and address as the thing
vertexToAddressDictionary = {}

#assigns a key with value of integer zero to equal HUB
vertexToAddressDictionary[0] = addressList[0][1]

#O(1)
for x in range(1,27):
        vertexToAddressDictionary[x] = addressList[x][1]

addressToVertexDictionary = {}
addressToVertexDictionary[addressList[0][1]] = 0

#O(1)
for x in range(27):
        addressToVertexDictionary[addressList[x][1]] = x
#print(addressToVertexDictionary)


package = packHash.search(20)
packageString = package.address
#print(addressToVertexDictionary[packageString])

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
                                if dist < min:
                                        min = dist
                                        nextFromAddress = packages
                                        nextBestAddress = package.address

                        newarray.append(nextFromAddress)
                        nextToAddress = nextBestAddress
        return newarray