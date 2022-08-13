# import csv
# from hash import *
# from package import *
#
# #Hashtable instance, created a hashtable called packHash
# """packHash, an instance of the hashtable class
# will store the key value pairs of all the packages
# that were passed in from the loadPackages function
# with the key being the PackageID"""
# packHash = Hashtable()
#
#
# #populates packHash with data read from the package csv and written to 40 Package instances
# def loadPackages(filename):
#     with open(filename, 'r') as packageDataFile:
#         packageData = csv.reader(packageDataFile, delimiter = ',')
#         next(packageDataFile)
#         for row in packageData:
#             pID = int(row[0]) #going into whatever number row first column
#             pAddress = row[1] #going into whatever number row 2nd column
#             pCity = row[2] #going into whatever number row 3rd column
#             pState = row[3] #going into whatever number row 4th column
#             pZip = row[4] #going into whatever number row 5th column
#             pDeadline = row[5] #going into whatever number row 6th column
#             pMass = row[6] #going into whatever number row 7th column
#             pNotes = row[7] #going into whatever number row 8th column
#             pStatus = "Loaded"
#
#             #for each row the above variables are being passed into an instance of the package class
#             pack = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus)
#
#             #insert the object into the hash function with the
#             packHash.insert(pID, pack)
#
#
# #calls load packages function and loads packHash the Hashtable that has the key value pairs of each
# loadPackages('WGUPS_Package_File.csv')
#
# def showPackages():
#     print("Packages in HashTable: \n")
#     for i in range(len(packHash.table)+1):
#         print("Package: {}".format(packHash.search(i+1)))
#
# def loadDistance(filename):
#     with open(filename, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter = ',')
#         next(csv_reader)
#         array = list(csv_reader)
#         return array
#
# #gets nested list of addresses from address.csv
# def loadAddresses(filename):
#     with open(filename, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         #next(csv_reader)
#         for row in csv_reader:
#             address = list(csv_reader)
#         return address
#
# #calls the loadAddress function and assigns it a variable
# addressList = loadAddresses('address.csv')
# #print(len(addressList))
#
#
# #dictionary that will hold the vertex values as the key and the addresses as the address as the value
# vertexToAddressDictionary = {}
# #starts the vertex 0 with hub
# vertexToAddressDictionary[0] = "HUB"
# #puts address values into dictionary
# for x in range(26):
#    vertexToAddressDictionary[x+1] = addressList[x][1]
#
#
# #print(vertexToAddressDictionary)
#
# #dictionay k = vertex v = address

import csv
from hash import *
from package import *

#Hashtable instance, created a hashtable called packHash
#packHash will store all the packages and their information
packHash = Hashtable()


#populates packHash with data from the package csv
def loadPackages(filename):
    with open(filename, 'r') as packages:
        packageData = csv.reader(packages, delimiter = ',')
        next(packages)
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pMass = package[6]
            pNotes = package[7]
            pStatus = "Loaded"

            #insert csv data into package object
            pack = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus)

            #insert the object into the hash function with the
            packHash.insert(pID, pack)


loadPackages('WGUPS_Package_File.csv')

def showPackages():
    print("Packages in HashTable: \n")
    for i in range(len(packHash.table)+1):
        print("Package: {}".format(packHash.search(i+1)))

def loadDistance(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        array = list(csv_reader)
        return array

#gets nested list of addresses from address.csv
def loadAddresses(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        address = list(csv_reader)
        return address


loadAddresses('address.csv')


#dictionay k = vertex v = address







