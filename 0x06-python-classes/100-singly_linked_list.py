#!/usr/bin/python3

class Node:
    """Class representing a node in a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The value of the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter and setter for the node's data."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter and setter for the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class representing a singly linked list."""
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new node with a given value in sorted order."""
        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node

        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            if temp.next_node:
                result += "\n"
            temp = temp.next_node
        return result
