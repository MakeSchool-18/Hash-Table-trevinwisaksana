#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def __iter__(self):
        """Allows the class to be iterable"""
        self.count = -1
        return self

    def next(self):
        '''Allows the iterable class to go iterate through elements'''
        if self.count < self.size:
            self.count += 1
        if self.count == self.size:
            raise StopIteration
        return self.as_list()[self.count]

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # Creates a new Node
        node = Node(item)
        # Checks if the LinkedList is empty
        if self.is_empty():
            # Adds the new node to the head
            self.head = node
        # If a tail already exists, add a new tail
        if self.tail is not None:
            self.tail.next = node
        # If a tail doesn't exist, add tail
        self.tail = node
        # Increments the size of the LinkedList
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # Creates a new Node
        node = Node(item)
        # Checks if the LinkedList is empty
        if self.is_empty():
            self.head = node
            self.tail = node
        # If a head already exists, create a variable that holds the head
        # This is so that we can still have access to the items in linked list
        temp, temp.next = self.head, self.head.next
        self.head, self.head.next = node, temp
        self.size += 1

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        current = self.head
        previous = None

        while current is not None: # While the list is not empty
            if current.data is item: # If the data matches an item in a head
                if self.head is current: # If the head data has the current item
                    self.head = current.next # Set the head pointer to None
                if self.tail is current: # If the item matches the tail data
                    self.tail = previous # Set the previous node to become the new tail
                if previous: # If previous is None (if it's the head)
                    previous.next = current.next # Set the head point to None
                return
            previous = current # Keep iterating
            current = current.next # Keep iterating

        return "Item not found" # Return item not found

        self.size -= 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        for item in self.as_list():
            if quality(item) is True:
                return item
            if quality(item) is None:
                raise ValueError("Item not found")


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
    ll.delete('A')
    print('tail: ' + str(ll.tail))
    print(ll)
    ll.delete('C')
    print("What's left: ", ll)
    print('tail: ' + str(ll.tail))
    ll.delete('B')
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
