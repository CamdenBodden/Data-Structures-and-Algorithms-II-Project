# Hash Table Creation
# Source: https://youtu.be/9HFbhPscPU0?si=gHU3zEBFiWbdb3cC (I used this video which was in the course tips to help with the creation of a Hash Table)
class HashTable:
    def __init__(self, initialCap=40):
        self.table = []
        for x in range(initialCap):
            self.table.append([])

    # Adds an item to the hash table or updates an item already in a list
    def insert(self, key, value):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]
        # Updates the key if it is already in the cell
        for kv in cell_list:
            # Prints the key value pair
            if kv[0] == key:
                kv[1] = value
                return True
        # If it is not in the cell, insert the value to the end of the list
        key_value = [key, value]
        cell_list.append(key_value)
        return True

    # This will search the hash table for a value with the matching key
    # Returns the value if found or None if it is not found
    def search(self, key):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]
        # search for key in cell
        for kv in cell_list:
            if kv[0] == key:
                return kv[1]
        return None

    # This will remove a value with an matching key from the hash table
    def remove(self, key):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]
        if key in cell_list:
            cell_list.remove(key)
