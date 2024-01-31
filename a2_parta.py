class HashTable:
    class Record:
        def __init__(self, key, val):
            """
            Initialize a Record with a key and value pair.

            Parameters:
            - key: The key of the record.
            - val: The value associated with the key.
            """
            self.key = key
            self.val = val

    def __init__(self, cap=32):
        """
        Initialize the HashTable with an optional initial capacity.

        Parameters:
        - cap: The initial capacity of the HashTable.
        """
        self.table = [None for _ in range(cap)]
        self.max_capacity = cap
        self.size = 0

    def insert(self, key, val):
        """
        Insert a key-value pair into the HashTable.

        Parameters:
        - key: The key to be inserted.
        - val: The value associated with the key.

        Returns:
        - True if the insertion is successful, False otherwise.
        """
        if self.search(key) is not None:
            return False

        self.size += 1
        q = hash(key)
        d = q % self.max_capacity

        while d < self.max_capacity * 2:
            if self.table[d % self.max_capacity] is None:
                self.table[d % self.max_capacity] = self.Record(key, val)
                break
            d += 1

        if len(self) >= self.max_capacity * 0.7:
            fresh_table = [None for _ in range(self.max_capacity * 2)]
            for q in range(self.max_capacity):
                fresh_table[q] = self.table[q]
            self.table = fresh_table
            self.max_capacity *= 2

        return True

    def modify(self, key, val):
        """
        Modify the value associated with a given key.

        Parameters:
        - key: The key to be modified.
        - val: The new value associated with the key.

        Returns:
        - True if modification is successful, False otherwise.
        """
        q = hash(key)
        d = q % self.max_capacity

        while d < self.max_capacity * 2:
            if self.table[d % self.max_capacity] is not None and self.table[d % self.max_capacity].key == key:
                self.table[d % self.max_capacity].val = val
                return True
            d += 1

        return False

    def remove(self, key):
        """
        Remove a key-value pair from the HashTable.

        Parameters:
        - key: The key to be removed.

        Returns:
        - True if removal is successful, False otherwise.
        """
        q = hash(key)
        d = q % self.max_capacity

        while d < self.max_capacity * 2:
            if self.table[d % self.max_capacity] is not None and self.table[d % self.max_capacity].key == key:
                self.table[d % self.max_capacity] = None
                self.size -= 1
                return True
            d += 1

        return False

    def search(self, key):
        """
        Search for the value associated with a given key.

        Parameters:
        - key: The key to search for.

        Returns:
        - The value associated with the key, or None if not found.
        """
        q = hash(key)
        d = q % self.max_capacity

        while d < self.max_capacity * 2:
            if self.table[d % self.max_capacity] is not None and self.table[d % self.max_capacity].key == key:
                return self.table[d % self.max_capacity].val
            d += 1

        return None

    def capacity(self):
        """
        Get the current capacity of the HashTable.

        Returns:
        - The current capacity.
        """
        return self.max_capacity

    def __len__(self):
        """
        Get the current size of the HashTable.

        Returns:
        - The current size.
        """
        return self.size
