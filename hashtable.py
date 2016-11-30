#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        # return 'HashTable({})'.format(self.length())
        return 'HashTable({})'.format(str(self.buckets))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        # return hash(key) % len(self.buckets)
        hash_value = 0 # hash is set to 0
        for char in key: # iterates through as much as the number of characters in key
            hash_value += ord(char) # return the unicode value to make the number different everytime
        return hash_value % len(self.buckets) # returns a number that will never be greater than the length of the bucket

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO: Count number of key-value entries in each of the buckets
        pass

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        hash_key = self._bucket_index(key) # Gets the index of the key

        if self.buckets[hash_key] is not None: # If the hask_key exists
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        hash_key = self._bucket_index(key) # Gets the index of the key

        if self.buckets[hash_key] is not None: # If the hask_key exists
            for key_value_pair in self.buckets[hash_key]: # Iteratre through the value pair
                if key_value_pair[0] is key: # If the key matches
                    return key_value_pair[1] # Return the value
        return None # If key doesn't exist, return None

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        hash_key = self._bucket_index(key) # Gets the key in the array
        key_value = (key, value) # Store tuple containing key and value in key_value

        if self.buckets[hash_key] is None: # Bucket returns None, the result of the hask_key, if empty
            self.buckets[hash_key] = list([key_value]) # Creates a new list based on the hash_key
            return True
        else: # If it's not empty
            for key_value_pair in self.buckets[hash_key]: # Goes through the key_value_pair
                if key_value_pair[0] is key: # If the key already exists, just update the value
                    key_value_pair[1] = value # Updates just the value
                    return True
            self.buckets[hash_key].append(key_value) # If the key doesn't exist, add the tuple
            return True


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        hash_key = self._bucket_index(key) # Storing the key inside the hash_key

        if self.buckets[hash_key] is None: # If we can't find the key
            return False
        for i in range(0, len(self.buckets[hash_key])): # Iterate through the amount of time until index
            if self.buckets[hash_key][i][0] is key: # If the key matches
                self.buckets[hash_key].pop(i) # Remove the key
                return True

    def keys(self):
        """Return a list of all keys in this hash table"""
        # TODO: Collect all keys in each of the buckets
        pass

    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        pass

def test_hashtable():
    ht = HashTable()
    print(ht)
    ht.set("Hello", 1)
    print(ht)
    ht.get("Hello")
    print(ht)
    ht.delete("Hello")
    print(ht)

if __name__ == "__main__":
    test_hashtable()
