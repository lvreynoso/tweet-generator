#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.list_length = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)
            self.temp = self.head

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        return self.generator()

    def generator(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next


    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        return self.list_length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        node = Node(item)
        # Append node after tail, if it exists
        if self.tail is not None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node 
            self.tail = node
        self.list_length += 1
        

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        node = Node(item)
        # Prepend node before head, if it exists
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = node 
            self.tail = node
        self.list_length += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality function
        match = None
        node = self.head
        while node is not None:
            if quality(node.data) is True:
                match = node.data 
                node = None
            else:
                node = node.next
        return match


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # raise ValueError('Item not found: {}'.format(item))
        previous = None
        found = False
        node = self.head
        while not found and node is not None:
            if node.data == item:
                # if we're not at the head, connect the previous node with the next one
                if previous is not None:
                    previous.next = node.next
                # if we ARE at the head, make the next node the head
                else:
                    self.head = node.next
                # if we're at the tail, point the tail to the previous node
                if node.next is None:
                    self.tail = previous
                self.list_length -= 1
                found = True
            previous = node
            node = node.next
        if not found:
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, comparator, replacement):
        # Walk through list until we find the target, then replace the data
        found = False
        node = self.head
        while not found and node is not None:
            if comparator(node.data) is True:
                node.data = replacement
                found = True
            node = node.next
        if not found:
            raise ValueError('Replacement target not found.')



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()