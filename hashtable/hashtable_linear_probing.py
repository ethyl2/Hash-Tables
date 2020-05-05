'''
Open Addressing: Linear Probing
-------------------------------
One option for the project this afternoon.
  "foo" hashes to index 1
  "bar" hashes to index 2
  "baz" hashes to index 2
  "qux" hashes to index 1
  "beej" hashes to index 2
  put("foo", 12)
  put("bar", 30)
  put("baz", 99)
  get("bar")
  get("baz")
  delete("bar")
  get("baz")
  put("bar", 30)
  get("beej")
  put("baz", 88)
  put("beej", 77)
  0     1           2           3             <-- index
[ None, ("foo",12), (None,30),  ("baz",88) ]
Put:
Scan forward from the hash index until we find either the key, or None
If we find a deleted slot along the way, keep it in mind
Put the value there
Get:
Scan forward from the hash index until we find either the key, or None
Return that
Delete:
Scan forward from the hash index until we find either the key, or None
If we find the key, mark it as deleted

'''


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.initial_capacity = capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        """
        FNV_prime = 2**40 + 2**8 + 0xb3
        hash = 14695981039346656037
        for x in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(x)
        return hash & 0xFFFFFFFFFFFFFFFF

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Scan forward from the hash index until we find either the key or go through the whole list.
        If the key is found, update the value. (In this case, since it uses tuples, replace the whole tuple).
        Otherwise, stick the new key-value tuple in the empty spot closest to the hashed index.
        If the storage list is full, print a message.
        For now, the index at which the tuple is stored is returned, or None is returned if the list is full.
        """
        index = self._hash_index(key)
        first_none = None
        new_entry = tuple([key, value])

        # Loop through entire list to see if key exists. It's faster to start with the index.
        # Loop through list from index to end
        for i in range(index, len(self.storage)):
            if first_none is None and self.storage[i] is None:
                first_none = i
            if self.storage[i] is not None and self.storage[i][0] == key:
                self.storage[i] = new_entry
                return i

        # If the key still wasn't found, loop through the beginning of list to the original_index
        for i in range(0, index):
            if first_none is None and self.storage[i] is None:
                first_none = i
            if self.storage[i] is not None and self.storage[i][0] == key:
                self.storage[i] = new_entry
                return i

        # At this point, the key wasn't found, so make a new entry. Put it into that list at first_none.
        self.size_check()
        if first_none is None:
            print('Storage is full. Time to increase capacity.')
            return None
        else:
            self.storage[first_none] = new_entry
            return first_none

    def get(self, key):
        """
        Go through the list to see if the key exists. Start at the hashed_index, because the key is more likely near it.
        Return the value if the key is found.
        Otherwise, go through the list from the beginning until the hashed_index.
        Return the value if the key is found.
        Otherwise, return None.
        """
        index = self._hash_index(key)
        for i in range(index, len(self.storage)):
            if self.storage[i] is not None and self.storage[i][0] == key:
                return self.storage[i][1]
        for i in range(0, index):
            if self.storage[i] is not None and self.storage[i][0] == key:
                return self.storage[i][1]
        return None

    def delete(self, key):
        """
        Go through the list to see if the key exists. Start at the hashed_index, because the key is more likely near it.
        Set the value at the current index to be None if the key is found.
        Otherwise, go through the list from the beginning until the hashed_index.
        Set the value at the current index to be None if the key is found.
        If the key still isn't found, return None.
        """
        index = self._hash_index(key)
        for i in range(index, len(self.storage)):
            if self.storage[i] is not None and self.storage[i][0] == key:
                self.storage[i] = None
                self.size_check()
                return i
        for i in range(0, index):
            if self.storage[i] is not None and self.storage[i][0] == key:
                self.storage[i] = None
                self.size_check()
                return i
        return None

    def size_check(self):
        '''
        Update your HashTable to automatically double in size when it grows past a load factor of 0.7
        and half in size when it shrinks past a load factor of 0.2.
        This (I assume the halving) should only occur 
        if the HashTable has been resized past the initial size.

        '''
        num_entries = sum(x is not None for x in self.storage)
        # print('num_entries: ' + str(num_entries))
        load_factor = num_entries/self.capacity
        # print('load factor: ' + str(load_factor))

        if load_factor > 0.7:
            print('Time to increase the capacity; load factor is ' + str(load_factor))
            self.resize()

        if self.capacity > self.initial_capacity:
            if load_factor < 0.2:
                print('time to shrink the hashtable in half')
                self.shrink()

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        """
        self.capacity = self.capacity * 2
        print("New capacity: " + str(self.capacity))
        self.make_new_storage()

    def make_new_storage(self):
        """
        Make a new list with length of the new capacity.
        Rehash each key and store key-values in new list
        """
        new_storage = [None] * self.capacity

        # Loop through the old storage and put each tuple into the new storage.
        for i in range(0, len(self.storage)):
            if self.storage[i] is not None:
                new_index = self._hash_index(self.storage[i][0])
                current_tuple = self.storage[i]
                # Loop through new_storage, starting at new_index, until an empty spot is found.
                spot_found = False
                for i in range(new_index, len(new_storage)):
                    if new_storage[i] is None:
                        new_storage[i] = current_tuple
                        spot_found = True
                        break

                # Loop through new_storage, starting at 0, until new_index, if an empty spot hasn't been found yet.
                if spot_found == False:
                    for i in range(0, new_index):
                        if new_storage[i] is None:
                            new_storage[i] = current_tuple
                            spot_found = True
                            break

        self.storage = new_storage

    def shrink(self):
        '''
        Halves the capacity of the hash table and
        rehashes all key/value pairs.
        '''
        self.capacity = self.capacity // 2
        self.make_new_storage()


ht = HashTable(10)
ht.put("First Entry", "Value 1")
ht.put("Second Entry", "Value 2")
ht.put("Third Entry", "Value 3")
ht.put("Fourth Entry", "Value 4")
ht.put("Fifth Entry", "Value 5")
ht.put("Sixth Entry", "Value 6")
ht.put("Sixth Entry", "New Value 6")
ht.put("Seventh Entry", "Value 7")
ht.put("Eighth Entry", "Value 8")
ht.put("Ninth Entry", "Value 9")
ht.put("Tenth Entry", "Value 10")
ht.put("Eleventh Entry", "Value 11")
# print(ht.storage)

# print(ht.get("Fifth Entry"))
# print(ht.get("Eleventh Entry"))
# print(ht.get("Sixth Entry"))
# print(ht.get("Hundreth Entry"))

print(ht.delete("First Entry"))
print(ht.get("First Entry"))
print(ht.delete("Thirtieth Entry"))

# ht.put("Eleventh Entry", "Value 11 fits this time")
# print(ht.get("Eleventh Entry"))
# ht.size_check()
print(ht.capacity)
print(ht.get("Fifth Entry"))
print(ht.get("Eleventh Entry"))
print(ht.get("Sixth Entry"))

ht.delete("Second Entry")
ht.delete("Third Entry")
ht.delete("Fourth Entry")
ht.delete("Fifth Entry")
ht.delete("Sixth Entry")
ht.delete("Seventh Entry")
ht.delete("Ninth Entry")
print(ht.capacity)
