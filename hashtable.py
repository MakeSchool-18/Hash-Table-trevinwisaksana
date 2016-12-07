#!python

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.size = 0
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
        return self.size
        # for bucket in self.buckets():

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        hash_key = self._bucket_index(key) # Gets the index of the key
        if self.buckets[hash_key].is_empty() is False: # If the hask_key exists
            for key_value_pair in self.buckets[hash_key]: # Iteratre through the value pair
                if key_value_pair[0] is key: # If the key matches
                    return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        hash_key = self._bucket_index(key) # Gets the index of the key

        if self.buckets[hash_key].is_empty() is False: # If the hask_key exists
            for key_value_pair in self.buckets[hash_key]: # Iteratre through the value pair
                if key_value_pair[0] is key: # If the key matches
                    return key_value_pair[1] # Return the value
        raise KeyError("Key doesn't exist") # If key doesn't exist, return None

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        hash_key = self._bucket_index(key) # Gets the key in the array
        key_value = (key, value) # Store tuple containing key and value in key_value
        bucket = self.buckets[hash_key]

        if bucket.find(lambda (tuple_key, _): tuple_key == key):
            self.delete(key) # Removing the key from the list
            return True

        bucket.append(key_value) # Append the new tuple
        self.size += 1 # Change the size because the delete reduces it by 2
        return True

        # Important example of repetition
        ''' if bucket.is_empty() is True: # Bucket returns None, the result of the hash_key, if empty
            self.size += 1 # Increments the size everytime set() is called
            bucket.append(key_value) # Creates a new list based on the hash_key
            return True
        # If bucket contains key
        elif bucket.find(lambda (tuple_key, _): tuple_key == key):
        # elif bucket.find(lambda (k, v): k == key):
        # elif bucket.find(lambda data: data[0] == key):
            self.delete(key) # Removing the key from the list
            bucket.append(key_value) # Append the new tuple
            self.size += 1 # Change the size because the delete reduces it by 2
            return True
        else: # Bucket contains key-value entry
            bucket.append(key_value) # If the key doesn't exist, add the tuple
            self.size += 1 # Increments the size everytime set() is called
            return True '''

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        self.size -= 1
        hash_key = self._bucket_index(key) # Gets the index of the key
        if self.contains(key) is True:
            for key_value_pair in self.buckets[hash_key]: # Iteratre through the value pair
                if key_value_pair[0] is key: # If the key matches
                    self.buckets[hash_key].delete(key_value_pair)
                    # self.buckets[hash_key] = None
                    return True
        else:
            raise KeyError("Key no longer exists") # If key doesn't exist, return None

    def keys(self):
        """Return a list of all keys in this hash table"""
        # TODO: Collect all keys in each of the buckets
        all_keys = [] # Will store all the key
        for bucket in self.buckets:
            for key in bucket:
                if key is not None:
                    all_keys.append(key[0])
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        all_values = [] # Will store all the key

        for bucket in self.buckets:
            for value in bucket:
                if value is not None:
                    all_values.append(value[1])
        return all_values


def test_hashtable():
    ht = HashTable()
    ht.set('I', 1)
    ht.set('V', 4)
    ht.set('X', 9)
    print ht.length()
    ht.set('V', 5)  # Update value
    ht.set('X', 10)  # Update value
    print ht
    ht.get('I')
    ht.get('V')
    ht.get('X')
    print ht.length()  # Check length is not overcounting

if __name__ == "__main__":
    test_hashtable()
