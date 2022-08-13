from distances import *
from package import *
from readcsv import *
from truck import *

addressList = loadAddresses('address.csv')
#print(addressList)









#
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