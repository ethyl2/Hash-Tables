# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        # First, get the hashed_key
        hashed_key = self._hash_mod(key)
        # For Part 1, check if hashed_key is already in hashtable. If so, generate an error warning.
        # If the hashed_key is not already in the hashtable, create a LinkedPair instance with its key and value.
        # For part 2, check if a LL already exists at that hashed_key index. If not, add the LinkedPair instance. If so, add the LinkedPair index to the end of the LL.
        '''
        hashed_key = self._hash_mod(key)
        # print(f'{key} is stored at {str(hashed_key)}')
        new_linked_pair = LinkedPair(key, value)

        node = self.storage[hashed_key]
        if node is None:
            self.storage[hashed_key] = new_linked_pair
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = new_linked_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Compute hash
        hashed_key = self._hash_mod(key)

        # Get the first node in LL in storage
        node = self.storage[hashed_key]

        # Traverse the linked list at this node until the key is found or the end is reached
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity

    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    '''
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
    '''
