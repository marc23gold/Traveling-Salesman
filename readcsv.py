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


loadAddresses('address1.csv')


#dictionay k = vertex v = address







