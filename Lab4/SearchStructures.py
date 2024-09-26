"""
 File name: python_Lab1.py
    Author: Kenneth Tabilas 
    Date created: 09/25/2024
    Python Version: 3.6.9 
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.__items = []

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        return len(self.__items) == 0

    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        self.__items.append(item)

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        if not self.isEmpty():
            return self.__items.pop()
        return None
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.__items = []

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
         return len(self.__items) == 0


    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
       self.__items.append(item)


    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        if not self.isEmpty():
            return self.__items.pop(0)
        return None
    
    