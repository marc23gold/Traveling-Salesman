#chaining hashtable class
class Hashtable:
    #constructor
    #O(1) time complexity because the bucket size is already set and is a constant
    #Space complexity: O(1)
    def __init__(self, bucket_size = 41):
        #use empty list as a container for the buckets
        self.table = []
        #for loop that initalizes all the empty buckets
        #inserting 40 empty arrays into an empty array so: [[][][]...[]]
        for i in range(bucket_size):
            self.table.append([])

    #Inserts a new item into the hash table.
    #Time complexity: O(N)
    #Space complexity: O(N)
    def insert(self, key, item):
        #hash function using modulus
        #bucket is being used as the index number for the table that contains
        #the 40 empty arrays so the function is using the modulus method
        bucket = int(key) % len(self.table)
        #index aka the bucket_list number is assigned from the bucket variable
        #which contains the hash function that deterens where the item will go
        bucket_list = self.table[bucket]


        key_value = [key, item]

        #update key if it is already in the bucket
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        # insert the item at the end of the bucket list
        bucket_list.append(key_value)
        return True
        # Searches for an item with matching key in the hash table.
        # Returns the item if found, or None if not found.

    # Time complexity: O(N)
    # Space complexity: O(1)
    """The average time complexity would be constant time but because out chaining and the possibility of a bucket having 
     more than
     than one key it's O(N)"""
    # Function gets the value from the key
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
        # search for the key in the bucket list
            if key_value[0] == key:
            # find the item's index and return the item that is in the bucket list.
                return (key_value[1])

        else:
            # the key is not found.
            return None



    #Time complexity: O(N)
    #Space complexity: O(N)
    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])








