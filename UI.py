#Basic UI call function from command line
#basic imports
import datetime

from readcsv import *
from truck import *

#Shows all the packages with a given deadline
#Time complexity: O(N)
#Space Complexity: O(N)
def showAllPackagesWithGivenDeadlineTime():
    user = input("Please put in the hour you want: ")
    userMinutes = input("Please put in the minute you want: ")
    userTime = datetime.timedelta(hours = int(user), minutes=int(userMinutes))
    # if the time is greater or equal to 10:20 then the package id on package nine will be corrected
    if userTime >= datetime.timedelta(hours=10, minutes=20):
        packageNine = packHash.search(9)
        packageNine.address = "410 S State St"
        packageNine.zip = "84103"
        packageNine.notes = "Address corrected"
    #going through all the packages in the Hashtable and adjusting the status depending on the time
    for x in range(1,41):
        allPacks = packHash.search(x)
        if allPacks.deliveryTime == None:
            pass
        elif allPacks.deliveryTime < userTime:
            allPacks.status = "Delivered"

        elif  userTime > allPacks.departureTime:
            allPacks.status = "In Route"
            allPacks.deliveryTime = None
        else:
            allPacks.status = "At the Hub"
            allPacks.deliveryTime = None

        print(allPacks)

    #total = (truck1.mileage + truck2.mileage + truck3.mileage)
    #print("\nThe total milage is: ",total)



#Gets the Packages in between a range of packages and shows whether they were delivered or not
#Time complexity: O(N)
#Space Complexity: O(N)
def startEnd():
    startUser = input("Please put in the start hour you want: ")
    startUserMinutes = input("Please put in the minute you want: ")
    endUser = input("Please put in the end hour you want: ")
    endUserMinutes = input("Please put in the minute that you want: ")

    begginingTime = datetime.timedelta(hours = int(startUser), minutes=int(startUserMinutes))
    endingTime = datetime.timedelta(hours = int(endUser), minutes=int(endUserMinutes))
    # if the time is greater or equal to 10:20 then the package id on package nine will be corrected
    if endingTime >= datetime.timedelta(hours=10, minutes=20):
        packageNine = packHash.search(9)
        packageNine.address = "410 S State St"
        packageNine.zip = "84103"
        packageNine.notes = "Address corrected"
    for x in range(1,41):
        allPacks = packHash.search(x)
        if allPacks.deliveryTime == None:
            pass
        if endingTime >= datetime.timedelta(hours=8, minutes=0):
            if allPacks.deliveryTime < endingTime :
                allPacks.status = "Delivered"

            elif allPacks.deliveryTime > endingTime and  allPacks.departureTime < endingTime:
                allPacks.status = "In Route"
                allPacks.deliveryTime = None
            else:
                allPacks.status = "At the Hub"
                allPacks.deliveryTime = None
        else:
            allPacks.status = "At the Hub"
            allPacks.deliveryTime = None


        print(allPacks)

    #total = (truck1.mileage + truck2.mileage + truck3.mileage)
    #print("\nThe total milage is: ",total)


#Shows a package delivery status
#Time complexity: O(N)
#Space Complexity: O(N)
def showIndividualPackages():
    user = input("Put in the hour you want: ")
    userMinutes = input("Put in the minute you want: ")
    packageId = input("Please put in the package id you want: ")
    userTime = datetime.timedelta(hours = int(user), minutes=int(userMinutes))
    # if the time is greater or equal to 10:20 then the package id on package nine will be corrected
    if userTime >= datetime.timedelta(hours=10, minutes=20):
        packageNine = packHash.search(9)
        packageNine.address = "410 S State St"
        packageNine.zip = "84103"
        packageNine.notes = "Address corrected"
    #going through all the packages in the Hashtable and adjusting the status depending on the time
    for x in range(1,41):
        allPacks = packHash.search(x)
        if allPacks.deliveryTime == None:
            pass
        elif allPacks.deliveryTime < userTime:
            allPacks.status = "Delivered"

        elif  userTime > allPacks.departureTime:
            allPacks.status = "In Route"
            allPacks.deliveryTime = None
        else:
            allPacks.status = "At the Hub"
            allPacks.deliveryTime = None

    print(packHash.search(int(packageId)))





