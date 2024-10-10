"""
Author: Kenneth Tabilas
Filename: myarray.py
Description: Implementation of an unsorted array with duplicates
"""

class MyArray:
    # Constructor
    def __init__(self, initialSizeorValues):
        # If the initial input is an integer (initial size)
        if isinstance(initialSizeorValues, int):
            self.__a = [None] * initialSizeorValues  # Creates a list filled with None
            self.__length = 0  # Sets the length to be 0 (empty elements)
            self.__addtoSize = initialSizeorValues  # Sets the size proportional to the initial size
        # If the initial input is a list (initial values)
        elif isinstance(initialSizeorValues, list):
            self.__a = initialSizeorValues  # Sets the array to the initial values
            self.__length = len(self.__a)  # Sets the length to the size of the initial list
            self.__addtoSize = len(self.__a)  # Sets the size proportional to the list input

    ########
    # Methods
    ########

    # Return the current length of the array
    def length(self):
        return self.__length

    # Return a list of the current array values
    def values(self):
        return self.__a[:self.__length]  # Only valid elements are considered

    # Return the value at index idx, or do not return anything if out of bounds
    def get(self, idx):
        if 0 <= idx < self.__length:  # Check if idx is in bounds
            return self.__a[idx]

    # Set the value at index idx
    def set(self, idx, value):
        if 0 <= idx < self.__length:  # Check if idx is in bounds
            self.__a[idx] = value

    # Insert value to the end of the array
    def insert(self, value):
        # Check if array is full
        if self.__length == self.__addtoSize:
            self.__addtoSize += 1  # Increment size of the array by one
            self.__a.append(None)  # Append None to expand the array
        
        # Set the new value at the end and increment the length
        self.__a[self.__length] = value
        self.__length += 1

    # Return the index of value in the array, or -1 if value is not found
    def search(self, value):
        # Only search the indices we've inserted
        for idx in range(self.__length):
            if self.__a[idx] == value:
                return idx
        return -1

    # Delete all occurrences of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        delallinstance = False  # To check if any value was deleted
        while True:
            # Find the index of the value to delete
            idx = self.search(value)
            if idx != -1:  # If value was found
                delallinstance = True
                self.__length -= 1  # Decrement the length
                
                # Shift all the remaining values
                for j in range(idx, self.__length):
                    self.__a[j] = self.__a[j + 1]
                
                self.__a[self.__length] = None  # Set the last element to None
            else:
                break  # No more duplicates found
        return delallinstance

    # Print all items in the array
    def traverse(self):
        for i in range(self.__length):
            print(self.__a[i])

if __name__ == '__main__':
    pass
