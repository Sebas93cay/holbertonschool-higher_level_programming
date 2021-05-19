#!/usr/bin/python3
"""
Singly linked list
class Node and class SinglyLinkedList
"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = None
            return
        if (type(value) is not Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """List class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        mynode = Node(value)
        if self.__head is None:
            self.__head = mynode
        else:
            h_node = self.__head
            if value < h_node.data:
                mynode.next_node = h_node
                self.__head = mynode
            else:
                while (h_node.next_node is not None):
                    if value < h_node.next_node.data:
                        break
                    h_node = h_node.next_node
                mynode.next_node = h_node.next_node
                h_node.next_node = mynode

    def __str__(self):
        if self.__head is None:
            return
        text = ""
        h_node = self.__head
        text = text+str(h_node.data)
        while(h_node.next_node is not None):
            h_node = h_node.next_node
            text = text+"\n"+str(h_node.data)
        return text
