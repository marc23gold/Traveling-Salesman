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


"""Uses the nearest neighbor algorithm to sort the packages already located in the truck"""
def algo (truck):
        #this array will hold the sorted address values that will later be turned back into the package number
        newarray = []
        #will get the next address from the address associated with current package
        nextToAddress = truck.address
        #i is the index of the list packages x is the package item
        #so for package items in truck.packages pass through the list of packages
        for i,x in enumerate(truck.packages):


                        #setting the minimum value to be a large number
                        min = 1000
                        #set the nextFromAddress initially to None
                        nextFromAddress = None
                        #set the nextBestAddress initially to None
                        nextBestAddress = None
                        #loop that passes through the truck array till a minimum value is found
                        for packages in truck.packages:
                                #if the package is already in the newarray continue to the next one
                                if packages in newarray:
                                        continue

                                package = packHash.search(packages)


                                dist = getDistanceTo(nextToAddress, package.address)

                                n = sum([1 for p in truck.packages if packHash.search(p).deadline != "EOD" and p not in newarray])
                                if n and package.deadline == "EOD":
                                    continue

                                """if the variable dist is less than the minimum which will be continuously reassigned to
                                the lowest value distance value found in the list then NextFrom Address and Next Best Address
                                will be assigned"""
                                if dist < min:
                                        min = dist
                                        nextFromAddress = packages
                                        nextBestAddress = package.address

                        newarray.append(nextFromAddress)
                        nextToAddress = nextBestAddress
        return newarray