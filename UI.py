#Basic UI call function from command line
#basic imports
import datetime

from readcsv import *
from truck import *

"""def UI(#whatever, whatever):
        if #condition on whether to print one statement or everyithg:
            #statements to print
        else:
            #print all state ments """
user = input("Please put in the time you want in the format: ")
userTime = datetime.timedelta(hours = int(user))
for x in range(1,41):
    allPacks =packHash.search(x)
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




