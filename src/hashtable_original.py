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

        The starting number 5381 was picked by Daniel J. Bernstein simply because testing showed 
        that it results in fewer collisions and better avalanching.
        The choice of 33 has never been adequately explained.

        ord(c)
        Given a string representing one Unicode character, 
        return an integer representing the Unicode code point of that character. 
        For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. 

        Multiplying hash by 33 could be performed by doing hash * 33. However, the function 
        instead uses (hash << 5) + hash bit shifts which is on many CPUs a faster way to perform this operation. 

        Bitwise Operators:
        x << y
        Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
        This is the same as multiplying x by 2**y.

        hash << 5 “shifts” the bits to the left by 5 spaces, multiplying the number by 32 (2^5) and + hash adds another value of hash, 
        turning this into multiplying by 33.

        x & y
        Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
        '''
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # return self._hash(key) % self.capacity
        # For stretch:
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        1. Get the hashed_key.
        hashed_key = self._hash_mod(key)

        2. Create a new LinkedPair instance.

        3. Grab the value stored in the LL storage at that hashed_key. If it is None, stick the LinkedPair instance there.

            Otherwise, traverse the LL until the current node has no .next property.

            Assign its .next property to point at the new LinkedPair instance.

        '''
        hashed_key = self._hash_mod(key)
        new_linked_pair = LinkedPair(key, value)

        node = self.storage[hashed_key]
        if node is None:
            self.storage[hashed_key] = new_linked_pair
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            prev.next = new_linked_pair

        else:
            # The key was found, so update the value
            node.value = value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        '''
        # Get the hashed_key.
        hashed_key = self._hash_mod(key)

        # Get the value stored in storage at that hashed_key.
        node = self.storage[hashed_key]

        # If that node is the desired one, point the storage[hashed_key] to its next.
        if node.key == key:
            self.storage[hashed_key] = node.next
            return

        # Traverse the LL until the key is found or the end of the LL is reached.

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print(f'{key} was not found')
            return None
        # Remove the LinkedPair node from the chain by assigning
        # the .next pointer of the previous node to be the node that its .next pointer was pointing to.
        prev.next = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

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

        '''
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity

        for i in range(len(self.storage)):
            # print(f'at index {i} in self.storage')
            node = self.storage[i]

            while node is not None:
                # traverse the LL to rehash each key/value pair
                # print("At key: " + str(node.key))
                hashed_key = self._hash_mod(node.key)
                new_storage[hashed_key] = node
                node = node.next
        self.storage = new_storage

    def print_report(self):
        for i in range(len(self.storage)):
            print('At index ' + str(i) + ':')
            node = self.storage[i]
            if node is None:
                print('Nothing at this index')
            else:
                while node is not None:
                    print(f'{node.key}: {node.value}')
                    node = node.next
            print('\n')


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

    print('')
    # Test remove
    ht.remove("line_3")
    print(ht.retrieve("line_3"))
    ht.insert("line_3", "Linked list saves the day!")
    print(ht.retrieve("line_3"))

    print('')
    ht.remove("line_1")
    print(ht.retrieve("line_1"))
    ht.insert("line_1", "Tiny hash table with a reinsert")
    print(ht.retrieve("line_1"))
    print('')

    # Test update
    ht.insert("line_1", "Tiny hash table with a value change")
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    ht.print_report()

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

    # Test for _hash_djb2
    # print(ht._hash_djb2('hello world'))
