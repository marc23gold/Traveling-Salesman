#Package class
class Package:
    #constructor
    # Time complexity: O(1)
    # Space complexity: O(1)
    def __init__(self, ID, address, city, state, zip, deadline, mass, notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        self.deliveryTime = None
    #Function that effects how strings will be shown
    # Time complexity: O(1)
    # Space complexity: O(1)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.notes, self.status, self.deliveryTime)