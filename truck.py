import datetime
from distances import *
from algo import *

#creating the truck class
#Time complexity: O(1)
#Space Complexity: O(1)
class Truck:
    def __init__(self,truckId, departure, address, mileage, packages):
        self.truckId = truckId
        self.departure = departure
        self.address = address
        self.mileage = mileage
        self.packages = packages

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.truckId, self.departure, self.address, self.mileage, self.packages)

#Creating instances of trucks one, two, and three
truck1 = Truck(1, datetime.timedelta(hours=8), 'HUB', 0.0, [13,39,14,15,34,16,19,20,21,1,30,8,40,4])
truck2 = Truck(2, datetime.timedelta(hours=8), 'HUB', 0.0, [37,38,5,3,18,36,2,33,7,29])
truck3 = Truck(3, datetime.timedelta(hours=9, minutes = 34), 'HUB', 0.0, [6,25,26,31,32,28,10,11,12,17,22,23,24,27,35,9])



#Function to return the distance between two addresses if the graph data structure were used, which it is not.
#a and b in the parameter represent the vertex numbers
#and will be passed into the function to find the distance
#Time complexity: O(1)
#Space Complexity: O(1)
def getDistance(a, b):
    distance = g.edge_weights[(vertex[a], vertex[b])]
    return distance

#function to find min distance/address if vertexes are used to find distance which they are not.
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




#function to deliver packages in a truck
#Time complexity: O(N)
#Space Complexity: O(N)
# loop truck package addresses and call getDistanceTo(fromAddress, stopAddress)
 #for all the addresses not visted yet
    #keep track of miles and time delivered
    #update delivery status and time delivered in Hash Table for the package delivered
    #and keep up with the total mileage and delivery times.
    """keep track of time by using:
        timeToDeliver(h) = distance(miles)/18(mph) where 18 mph average Truck speed
        time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).
        time_obj could be cumulated to keep track of time"""
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







#sorts the packages in the trucks using the nearest neighbor alogrithm to the a more optimal solution
truck1.packages = algo(truck1)
truck2.packages = algo(truck2)
truck3.packages = algo(truck3)


#delivering packages and keeping track of changing mileage and time
truckDeliverPakcages(truck1)
truckDeliverPakcages(truck2)
truckDeliverPakcages(truck3)
