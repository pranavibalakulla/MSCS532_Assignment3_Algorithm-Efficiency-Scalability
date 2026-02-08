class Node:
    """
    Node class to store a key-value pair in the hash table.
    Each node points to the next node in the chain (linked list) for collision handling.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to the next node in the chain


class HashTable:
    """
    Hash table implementation using chaining to resolve collisions.
    Supports insert, search, and delete operations efficiently.
    """
    def __init__(self, size=10):
        self.size = size  # Number of buckets in the hash table
        self.table = [None] * size  # Initialize buckets as empty
        self.count = 0  # Track number of key-value pairs in the table

    def _hash(self, key):
        """
        Simple hash function to compute an index for a given key.
        Can be replaced with a universal hash function for fewer collisions.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        """
        index = self._hash(key)
        node = self.table[index]

        # Traverse the chain to check if key already exists
        while node:
            if node.key == key:
                node.value = value  # Update existing key
                return
            node = node.next

        # Insert new node at the head of the chain
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.count += 1

    def search(self, key):
        """
        Search for a key in the hash table and return its value.
        Returns None if the key is not found.
        """
        index = self._hash(key)
        node = self.table[index]

        # Traverse the chain to find the key
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None  # Key not found

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        Returns True if deletion is successful, False if key is not found.
        """
        index = self._hash(key)
        node = self.table[index]
        prev = None

        # Traverse the chain to find the key
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next  # Remove node from chain
                else:
                    self.table[index] = node.next  # Node is head of chain
                self.count -= 1
                return True
            prev = node
            node = node.next
        return False  # Key not found


# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("apple", 10)   # Insert key-value pair
    ht.insert("banana", 20)
    print(ht.search("apple"))  # Output: 10
    ht.delete("apple")         # Delete a key
    print(ht.search("apple"))  # Output: None
