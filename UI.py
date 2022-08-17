#Basic UI call function from command line
#basic imports
import datetime

from readcsv import *
from truck import *

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
    else:
        allPacks.status = "At the Hub"

    print(allPacks)

total = (truck1.mileage + truck2.mileage + truck3.mileage)
print("\nThe total milage is: ",total)




