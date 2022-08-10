import csv
from  hash import *

#package class
class Package:
    #constructor
    #change values later
    def __init__(self, ID, address, city, state, zip, deadline, mass, notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status

    #function that effects how strings will be shown
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.notes, self.status)

#Hashtable instance
packHash = Hashtable()

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

"""print("Packages in HashTable: \n")
for i in range(len(packHash.table)+1):
    print("Package: {}".format(packHash.search(i+1)))"""

def loadDistance():
    with open("WGUPS_Distance_Table.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        array = list(csv_reader)
        return array








