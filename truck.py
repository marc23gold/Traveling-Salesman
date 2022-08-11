import datetime
from distances import *

class Truck:
    def __init__(self,truckId, departure, address, mileage, packages):
        self.truckId = truckId
        self.departure = departure
        self.address = address
        self.mileage = mileage
        self.packages = packages

truck1 = Truck(1, datetime.timedelta(hours=8), vertex[0], 0.0, [13,14,15,16,17,19,1,2,4,5,7,8,10,11,12,20])
truck2 = Truck(2, datetime.timedelta(hours=8), vertex[0], 0.0, [3,9,18,21,22,23,24,26,27,29,30,31,33,34])
truck3 = Truck(3, datetime.timedelta(hours=8), vertex[0], 0.0, [6,25,28,32,35,36,37,38,39,40])