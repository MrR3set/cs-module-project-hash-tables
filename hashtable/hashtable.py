class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity>MIN_CAPACITY:
            self.capacity=capacity
            self.arr = [None] * self.capacity
        else:
            self.capacity=MIN_CAPACITY
            self.arr = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.arr)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hsh = 0x811c9dc5
        fnv_32_prime = 0x01000193
        for byte in key:
            hsh = hsh ^ ord(byte)
            hsh = (hsh*fnv_32_prime)%self.capacity
        return hsh

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hsh = 5381
        for x in key:
            hsh = (( hsh << 5) + hsh) + ord(x)
    
        return hsh & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) 
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Get the index at which we will be going to insert the value
        index = self.hash_index(key)
        # Check if the desired index is empty or not
        if self.arr[index] is None:
            self.arr[index] = HashTableEntry(key,value)
        else:
            # If the index is not empty we have to iterate until we find that .next is None
            curr = self.arr[index]

            while curr.next:
                # Check if the value has changed
                if curr.value != value and curr.key == key:
                    print("Rewriting value", value)
                    curr.value = value
                    return
                else:
                    curr = curr.next          
            if curr.value != value and curr.key == key:
                print("Rewriting value", value)
                curr.value = value
            else:
                print("Writing value at", index, value)
                curr.next = HashTableEntry(key,value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # Check if the desired index is empty or not
        if self.arr[index] is None:
            return None
        elif self.arr[index].key == key:            
            # Check if there is a linked list
            if self.arr[index].next is not None:
                self.arr[index] = self.arr[index].next
            else:
                self.arr[index] = None
        else:
            # If the index is not empty we have to iterate until we find that .next is None
            curr = self.arr[index]
            prev = None
            while curr.next:
                # Check if the value has changed
                if curr.key == key:
                    prev = curr.next
                    curr = None
                    return
                else:
                    prev = curr
                    curr = curr.next          
            if curr.key == key:
                prev = curr.next
                curr = None
            else:
                return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.arr[index] is None:
            return None
        curr = self.arr[index]
        while curr is not None:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.next
        return None
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
