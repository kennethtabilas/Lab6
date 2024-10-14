"""
ENGR 221 - Lab 5
Author: Kenneth Tabilas
Date: October 13, 2024
"""

from .doubleNode import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__firstNode = None
        self.__lastNode = None 

    def isEmpty(self):
        return self.__firstNode is None

    def first(self):
        if self.isEmpty():
            raise Exception("The list is empty.")
        return self.__firstNode.getValue()

    def getFirstNode(self):
        return self.__firstNode

    def getLastNode(self):
        return self.__lastNode

    def setFirstNode(self, node):
        if not isinstance(node, DoubleNode) and node is not None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        self.__firstNode = node

    def setLastNode(self, node):
        if not isinstance(node, DoubleNode) and node is not None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        self.__lastNode = node

    def find(self, value):
        current = self.__firstNode
        while current:
            if current.getValue() == value:
                return current
            current = current.getNextNode()
        return None

    def insertFront(self, value):
        new_node = DoubleNode(value)
        if self.isEmpty():
            self.__firstNode = new_node
            self.__lastNode = new_node
        else:
            new_node.setNextNode(self.__firstNode)
            self.__firstNode.setPreviousNode(new_node)
            self.__firstNode = new_node

    def insertBack(self, value):
        new_node = DoubleNode(value)
        if self.isEmpty():
            self.__firstNode = new_node
            self.__lastNode = new_node
        else:
            new_node.setPreviousNode(self.__lastNode)
            self.__lastNode.setNextNode(new_node)
            self.__lastNode = new_node

    def insertAfter(self, value_to_add, after_value) -> None:
        current = self.find(after_value)
        if current is None:
            return False
        new_node = DoubleNode(value_to_add)
        next_node = current.getNextNode()
        new_node.setNextNode(next_node)
        new_node.setPreviousNode(current)
        current.setNextNode(new_node)
        if next_node:
            next_node.setPreviousNode(new_node)
        else:
            self.__lastNode = new_node

    def deleteFirstNode(self):
        if self.isEmpty():
            raise Exception("The list is empty.")
        value = self.__firstNode.getValue()
        if self.__firstNode == self.__lastNode:
            self.__firstNode = None
            self.__lastNode = None
        else:
            self.__firstNode = self.__firstNode.getNextNode()
            self.__firstNode.setPreviousNode(None)
        return value

    def deleteLastNode(self):
        if self.isEmpty():
            raise Exception("The list is empty.")
        value = self.__lastNode.getValue()
        if self.__firstNode == self.__lastNode:
            self.__firstNode = None
            self.__lastNode = None
        else:
            self.__lastNode = self.__lastNode.getPreviousNode()
            self.__lastNode.setNextNode(None)
        return value

    def deleteValue(self, value):
        node_to_delete = self.find(value)
        if node_to_delete is None:
            return None
        if node_to_delete == self.__firstNode:
            return self.deleteFirstNode()
        elif node_to_delete == self.__lastNode:
            return self.deleteLastNode()
        else:
            previous_node = node_to_delete.getPreviousNode()
            next_node = node_to_delete.getNextNode()
            previous_node.setNextNode(next_node)
            next_node.setPreviousNode(previous_node)
            return node_to_delete.getValue()

    def forwardTraverse(self):
        current = self.__firstNode
        while current:
            print(current.getValue(), end=" <-> ")
            current = current.getNextNode()
        print("None")

    def reverseTraverse(self):
        current = self.__lastNode
        while current:
            print(current.getValue(), end=" <-> ")
            current = current.getPreviousNode()
        print("None")

    def __len__(self):
        count = 0
        current = self.__firstNode
        while current:
            count += 1
            current = current.getNextNode()
        return count

    def __str__(self):
        values = []
        current = self.__firstNode
        while current:
            values.append(str(current.getValue()))
            current = current.getNextNode()
        return " <-> ".join(values)
