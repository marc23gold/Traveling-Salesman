import datetime
from distances import *
from algo import *

class Truck:
    def __init__(self,truckId, departure, address, mileage, packages):
        self.truckId = truckId
        self.departure = departure
        self.address = address
        self.mileage = mileage
        self.packages = packages

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.truckId, self.departure, self.address, self.mileage, self.packages)

truck1 = Truck(1, datetime.timedelta(hours=8), 'HUB', 0.0, [14,15,16,34,17,19,1,4,13,5,7,8,10,11,12])
truck2 = Truck(2, datetime.timedelta(hours=8), 'HUB', 0.0, [3,18,20,21,22,23,24,27,29,30,31,32,33])
truck3 = Truck(3, datetime.timedelta(hours=9, minutes = 17), 'HUB', 0.0, [6,25,28,35,36,37,38,39,40,26,2,9])



#checks packages from the array and gives what is the next destination



#check and sort
#truck?.packages
#def checkPackages(packagelist):


#Function to return the distance between two addresses
#a and b in the parameter represent the vertex numbers
#and will be passed into the function to find the distance
def getDistance(a, b):
    distance = g.edge_weights[(vertex[a], vertex[b])]
    return distance

    #function to find min distance/address:
    """"inputs need to be the fromAddress or the address the truck is currently at
    to the address that is listed on the packages next in the list"""
def minDistanceFrom(fromAddress, toAddress):
    addresslist = []
    for x in range(27):
        addresslist.append(getDistance(int(fromAddress),int(x)))
        #deleting this specific index because it would be 0.0 and refers to the
        #fromAddress going to the fromAddress
        del addresslist[fromAddress]
        ok = min(addresslist)
        ad = addresslist.index(ok)
        alright = [ad+1, ok]
        return alright


#(minDistanceFrom(5))

#function to deliver packages in a truck
def truckDeliverPakcages(truck):
    truckTime = truck.departure
    for x in truck.packages:
        stop = packHash.search(x)
        d = getDistanceTo(truck.address, stop.address) #distance between to and go
        truck.mileage += d
        truck.address = stop.address
        truckTime = truckTime + datetime.timedelta(hours = d/18)
        stop.deliveryTime = truckTime
        stop.departureTime = truck.departure


    #loop truck package addresses and call minDistanceFrom(fromAddress, truckPackages)
    #for all the addresses not visted yet
    #keep track of miles and time delivered
    #update delivery status and time delivered in Hash Table for the package delivered
    #and keep up with the total mileage and delivery times.
    """keep track of time by using:
        timeToDeliver(h) = distance(miles)/18(mph) where 18 mph average Truck speed
        time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).
        time_obj could be cumulated to keep track of time"""


#truckSortPackage(truck1)
truck1.packages = algo(truck1)
truck2.packages = algo(truck2)
truck3.packages = algo(truck3)

#delivering packages
truckDeliverPakcages(truck1)
truckDeliverPakcages(truck2)
truckDeliverPakcages(truck3)
