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

    startUserTime = datetime.timedelta(hours = int(startUser), minutes=int(startUserMinutes))
    endUserTime = datetime.timedelta(hours = int(endUser), minutes=int(endUserMinutes))
    for x in range(1,41):
        allPacks = packHash.search(x)
        if allPacks.deliveryTime == None:
            pass
        elif allPacks.deliveryTime < endUserTime :
            allPacks.status = "Delivered"

        elif (allPacks.deliveryTime > endUserTime) and allPacks.departureTime < startUserTime:
            allPacks.status = "In Route"
            #allPacks.deliveryTime = None
        else:
            allPacks.status = "At the Hub"
            #allPacks.deliveryTime = None



        print(allPacks)

    #total = (truck1.mileage + truck2.mileage + truck3.mileage)
    #print("\nThe total milage is: ",total)



def showIndividualPackages():
    user = input("Put in the hour you want: ")
    userMinutes = input("Put in the minute you want: ")
    packageId = input("Please put in the package id you want: ")
    userTime = datetime.timedelta(hours = int(user), minutes=int(userMinutes))
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





