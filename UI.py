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

userTime = datetime.timedelta(hours = 11)
for x in range(1, 41):
    allPacks = packHash.search(x)
    if allPacks.deliveryTime < userTime:
        allPacks.status = "Delivered"
    elif  userTime > allPacks.departureTime:
        allPacks.status = "In Route"
    else:
        allPacks.status = "At the Hub"

    print(allPacks)

total = (truck1.mileage + truck2.mileage + truck3.mileage)
print(total)

