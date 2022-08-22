import csv
from hash import *
from package import *

#Hashtable instance, created a hashtable called packHash
#packHash will store all the packages and their information
packHash = Hashtable()


#Reads from the CSV file and populates packHash with data from the csv
#Time complexity: O(N^2)
#Space Complexity: O(N)
def loadPackages(filename):
    #Reads the CSV
    with open(filename, 'r') as packages:
        packageData = csv.reader(packages, delimiter = ',')
        #Skips the first row of the CSV
        next(packages)
        #Retrieves the columns of the given row and assigns data to variables
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

            #insert the object into the hash function with the insert
            packHash.insert(pID, pack)


loadPackages('WGUPS_Package_File.csv')

#Test function that shows the packages that have been loaded into the HashTable from the loadPakages function
#Time complexity: O(N)
#Space Complexity: O(1)
def showPackages():
    print("Packages in HashTable: \n")
    for i in range(len(packHash.table)+1):
        print("Package: {}".format(packHash.search(i+1)))


#Function gets data from a csv file writes to a list and returns the list
#Time complexity: O(N)
#Space Complexity: O(N)
def loadDistance(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        array = list(csv_reader)
        return array

#Gets nested list of addresses from address.csv
#Time complexity: O(N)
#Space Complexity: O(N)
def loadAddresses(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        address = list(csv_reader)
        return address


loadAddresses('address1.csv')


#dictionay k = vertex v = address







