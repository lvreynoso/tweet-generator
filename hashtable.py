#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.number_of_entries = 0
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __getitem__(self, key):
        # get an item with subscripting syntax
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self.number_of_entries

    def __iter__(self):
        return self.generator()

    def generator(self):
        for bucket in self.buckets:
            for entry in bucket:
                yield entry

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) always, since we have to traverse every single list node"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) always, since we have to traverse every single list node"""
        # Loop through all buckets
        # Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) always, since we have to traverse every single list node"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(1) to return a stored variable"""
        return self.number_of_entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n) since we are traversing a linked list"""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        found = False
        key_value = self.buckets[index].find(lambda item: item[0] == key)
        if key_value is not None:
            found = True
        return found

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n) since we are traversing a linked list"""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, return value associated with given key
        # Otherwise, raise error to tell user get failed
        # raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        key_value = self.buckets[index].find(lambda item: item[0] == key)
        if key_value is None:
            raise KeyError('Key not found: {}'.format(key))
        return key_value[1]

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(n) since we are traversing a linked list in the
        replace function"""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, update value associated with given key
        # Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key)
        key_value = (key, value)
        try:
            self.buckets[index].replace(lambda item: item[0] == key, key_value)
        except ValueError:
            self.buckets[index].append(key_value)
            self.number_of_entries += 1


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n) since we are traversing a linked list"""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, delete entry associated with given key
        # Otherwise, raise error to tell user delete failed
        # raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        key_value = self.buckets[index].find(lambda item: item[0] == key)
        if key_value is None:
            raise KeyError('Key not found: {}'.format(key))
        else:
            self.buckets[index].delete(key_value)
            self.number_of_entries -= 1


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()