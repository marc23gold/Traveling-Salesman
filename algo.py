from distances import *
from package import *
from readcsv import *




"""Uses the nearest neighbor algorithm to sort the packages already located in the truck"""
#checks packages from the list and gives what is the next package and destination
#Time complexity: O(N^2)
#Space Complexity: O(N)
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

                                #assigning the searched packages values from the HashTable instance to package
                                package = packHash.search(packages)

                                #calling the getDistance to function to get the distance between the next package and current package
                                dist = getDistanceTo(nextToAddress, package.address)

                                # assigning n with 1 with the package is in the truck and the deadline is not EOD and not already in the sorted list
                                n = sum([1 for p in truck.packages if packHash.search(p).deadline != "EOD" and p not in newarray])
                                #skips the package if it is n and the package deadline is EOD
                                if n and package.deadline == "EOD":
                                    continue

                                """if the variable dist is less than the minimum which will be continuously reassigned to
                                the lowest value distance value found in the list then NextFrom Address and Next Best Address
                                will be assigned"""
                                if dist < min:
                                        min = dist
                                        nextFromAddress = packages
                                        nextBestAddress = package.address
                        #adds the package to the sorted list
                        newarray.append(nextFromAddress)
                        #the next address to go to is assigned with the value of the next Best Address
                        nextToAddress = nextBestAddress
        #return the sorted list of addresses that optimizes for mileage and package deadlines
        return newarray


"""This is all for an alternative where the graph data structure were to be used"""
addressList = loadAddresses('address.csv')

#dictionary that will have index as the key and address as the thing
vertexToAddressDictionary = {}

#assigns a key with value of integer zero to equal HUB
vertexToAddressDictionary[0] = addressList[0][1]

#populates the dictionary with values
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