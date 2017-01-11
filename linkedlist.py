#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data # Constant running time to set data into data
        self.next = None # Constant running time to set to None

    def __repr__(self):
        """Returtvn a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None # O(1) constant running time
        self.tail = None # O(1) constant running time
        self.size = 0 # O(1) constant running time
        if iterable:
            for item in iterable: # O(n) running time
                self.append(item) # O(n) + O(1) running time

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def __iter__(self):
        """Allows the class to be iterable"""
        self.count = -1 # O(1) constant running time
        return self

    def next(self):
        '''Allows the iterable class to go iterate through elements'''
        if self.count < self.size: # Constant runtime
            self.count += 1 # Constant runtime
        if self.count == self.size:
            raise StopIteration
        return self.as_list()[self.count]

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = [] # Constant runtime
        current = self.head # Constant runtime

        # Best case and worst case runtime: (n) and O(n)
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        '''O(1), constant running time'''
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        return self.size # O(1) constant running time

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # Creates a new Node
        node = Node(item) # O(1) + O(1)
        # Checks if the LinkedList is empty
        if self.is_empty(): # O(1) constant running time
            # Adds the new node to the head
            self.head = node # O(1) * 3
        # If a tail already exists, add a new tail
        if self.tail is not None: # O(1) constant runtime
            self.tail.next = node # O(1) constant runtime
        # If a tail doesn't exist, add tail
        self.tail = node # Constant runtime
        # Increments the size of the LinkedList
        self.size += 1 # Constant runtime

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # Creates a new Node
        node = Node(item) # O(1) * 4
        # Checks if the LinkedList is empty
        if self.is_empty(): # O(1) constant runtime
            self.head = node
            self.tail = node
        # If a head already exists, create a variable that holds the head
        # This is so that we can still have access to the items in linked list
        temp, temp.next = self.head, self.head.next # O(1) * 4
        self.head, self.head.next = node, temp # O(1) * 4
        self.size += 1

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        current = self.head # Constant runtime
        previous = None # Constant runtime

        '''Best case and worst case runtime:  (n) and O(n)'''
        while current is not None: # While the list is not empty
            '''Best case and worst case runtime(respectively): (1) and O(n)'''
            if current.data is item: # If the data matches an item in a head
                '''Best case and worst case runtime: O(1)'''
                if self.head is current: # If the head data has the current item
                    '''Best case and worst case runtime: O(n) * 3'''
                    self.head = current.next # Set the head pointer to None
                '''Best case and worst case runtime: O(1)'''
                if self.tail is current: # If the item matches the tail data
                    '''Best case and worst case runtime: O(1) * 2'''
                    self.tail = previous # Set the previous node to become the new tail
                '''Best case and worst case runtime: O(1)'''
                if previous: # If previous is None (if it's the head)
                    previous.next = current.next # Set the head point to None
                return
            previous = current # Keep iterating
            current = current.next # Keep iterating

        '''Constant running time to return String'''
        return "Item not found"  # Return item not found

        '''Constant running time to decrement'''
        self.size -= 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
           # Best case running time:
           # (1) if item is near the head
           # Worst case running time:
           # O(n) if item cannot be found.
           # O(n) if item is near or at the tail

        # TODO: find item where quality(item) is True
        for item in self.as_list(): # O(n) if item is near the head
            if quality(item) is True: # Constant running time to return True
                return item # Constant time to return item
            if quality(item) is None: # O(n) running time
                raise ValueError("Item not found") # Constant time to raise error


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())
    '''
    print("===================")
    ll.prepend('C')
    ll.prepend('B')
    ll.prepend('A')
    print('List: ', ll)
    print('tail ', ll.tail)
    print("===================")
    '''
    print(">>>>>>>>>>>>>>>>>>>>")
    print(ll)
    ll.find(lambda item: item == 'D')
    print('List: ', ll)
    print(">>>>>>>>>>>>>>>>>>>>")

    print("-------------------")
    print(ll)
    ll.delete('C')
    print('tail: ' + str(ll.tail))
    print(ll)
    ll.delete('B')
    print("What's left: ", ll)
    print('tail: ' + str(ll.tail))
    ll.delete('A')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())
    print("-------------------")
    '''
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    for data in ll:
        print(data)
    '''
if __name__ == '__main__':
    test_linked_list()
