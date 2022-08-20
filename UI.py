#Basic UI call function from command line
#basic imports
import datetime

from readcsv import *
from truck import *

def showAllPackagesWithGivenDeadlineTime():
    user = input("Please put in the hour you want: ")
    userMinutes = input("Please put in the minute you want: ")
    userTime = datetime.timedelta(hours = int(user), minutes=int(userMinutes))
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

    total = (truck1.mileage + truck2.mileage + truck3.mileage)
    print("\nThe total milage is: ",total)




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
        elif allPacks.deliveryTime >= startUserTime and allPacks.deliveryTime <= endUserTime:
            allPacks.status = "Delivered"

        elif startUserTime > allPacks.departureTime:
            pass
        else:
            allPacks.deliveryTime = ""
            allPacks.ID = ""
            allPacks.address = ""
            allPacks.city = ""
            allPacks.state = ""
            allPacks.zip = ""
            allPacks.deadline = ""
            allPacks.mass = ""
            allPacks.notes = ""
            allPacks.status = ""


        print(allPacks)

    total = (truck1.mileage + truck2.mileage + truck3.mileage)
    print("\nThe total milage is: ",total)

startEnd()


