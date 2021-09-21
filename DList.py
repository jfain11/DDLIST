#!/usr/bin/env python3

# ----------------------------------------------------------------------
# DList.py
# Jacob Fain
# 09/21/2021
# ----------------------------------------------------------------------

from collections.abc import Iterable
from DListNode import *


class DList:
    # reference to node containing first item in the list
    head: Optional[DListNode]
    # reference to node containing the last item in the list
    tail: Optional[DListNode]
    # number of items in the list
    size: int

    # ------------------------------------------------------------------

    def __init__(self, seq: Iterable = ()):
        """
        initializes a list with the items in seq
        :param seq: the items to put in the list
        """
        self.head = None
        self.tail = None
        self.size = 0

        for x in seq:
            self.append(x)

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """returns number of items in the list"""
        return self.size

    # ------------------------------------------------------------------

    def __iter__(self):
        """iterates over each item in the list"""
        node = self.head
        # while not at end of list
        while node is not None:
            yield node.item
            # move to next node
            node = node.next

    # ------------------------------------------------------------------

    def __copy__(self):
        """returns shallow copy of the list (new nodes but same items)"""
        return DList(self)

    # ------------------------------------------------------------------

    def _find(self, position: int) -> DListNode:
        """
        :param position: index from -length to length -1; raises IndexError if position out of range
        :return: node at the specified position or raises IndexError if position is out of range
        """
        # if position is out of range, raises IndexError
        if position > self.size - 1:
            raise IndexError
        elif position < self.size - (self.size * 2):
            raise IndexError

        # retrieves the node at the list
        currentNode = self.head
        # initializes an accumulator for the index
        currentIndex = 0

        # if the position is negative, then makes the currentIndex 0 - size
        if position < 0:
            currentIndex = 0 - self.size

        # loops through each node in the list
        for i in range(self.size):
            # if the position and currentIndex match, then return the node
            if currentIndex == position:
                return currentNode

            # if they don't match, then move on to the next node and increment currentIndex
            else:
                currentIndex += 1
                currentNode = currentNode.next

    # ------------------------------------------------------------------

    def __getitem__(self, position: int) -> Item:
        """
        :param position: index to get the item at; raises IndexError if position out of range
        :return: item at the index specified by the position
        """
        # uses _find to retrieve the node at the position
        node = self._find(position)
        # returns the item stored in the node
        return node.item

    # ------------------------------------------------------------------

    def __setitem__(self, position: int, value: Item):
        """
        set the value at the specified position; raises IndexError if position out of range
        :param position: index to set the value at
        :param value: value to put at the position
        :return: None
        """
        # calls _find to retrieve the node at the position
        node = self._find(position)
        # changes the value of the node
        node.item = value

    # ------------------------------------------------------------------

    def __delitem__(self, position: int):
        """
        removes the node and item at the specified position from the list; raises IndexError if position out of range
        :param position: index of item/node to delete
        :return: None
        """
        # calls _delete to remove the node
        a = self._delete(position)

    # ------------------------------------------------------------------

    def _delete(self, position: int) -> Item:
        """
        removes the value/node at the specified position and returns the value at the node; raises IndexError
        if position out of range
        :param position:index of item/node to delete
        :return: the value at the specified position that was removed
        """
        # if the position is out of range, then raise IndexError
        if position < 0 - self.size or position > self.size - 1:
            raise IndexError

        # finds the node at the index
        node = self._find(position)
        item = node.item

        # if removing the head
        if position == 0 or position == 0 - self.size:
            tempNode = node.next
            node.next = None
            tempNode.prev = None
            self.head = tempNode
            self.size -= 1

        # if removing the tail
        elif position == self.size - 1 or position == -1:
            tempNode = node.prev
            node.prev = None
            tempNode.next = None
            self.tail = tempNode
            self.size -= 1


        # else if removing from the middle of the list
        else:
            prevNode = node.prev
            nextNode = node.next
            node.next = None
            node.prev = None
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.size -= 1

        # return the item that was removed
        return item


    # ------------------------------------------------------------------

    def clear(self):
        """
        removes all element from the list
        :return: None
        """
        # set the head and tail to None, and set the size to 0
        self.tail = None
        self.head = None
        self.size = 0

    # ------------------------------------------------------------------

    def append(self, x: Item):
        """
        adds the value x onto the end of the list
        :param x: value to add to the end of the list
        :return: None
        """
        if self.size == 0:
            self.head = self.tail = DListNode(x)

        else:
            # add node after the tail
            self.tail.next = DListNode(x, self.tail)
            # move tail to the new node
            self.tail = self.tail.next

        self.size += 1

    # ------------------------------------------------------------------

    def insert(self, position: int, x: Item):
        """
        inserts x at the index (positive or negative) at the specified position; note if position
        is beyond the end, it adds to the end of the list or if position is beyond the beginning, it inserts
        at the beginning
        :param position: index to insert at
        :param x: value to insert at the specified position
        :return: None
        """

        # if list is empty, use append
        if self.size == 0:
            self.append(x)

        # if the position is beyond the end, use append
        elif position > self.size - 1:
            self.append(x)

        else:
            # if the position is beyond the beginning, insert position at head
            if position < 0:
                position = 0

            # use _find to retrieve the node at the position
            node = self._find(position)

            # make a new DListNode to insert into the list
            newNode = DListNode(x)

            # if inserting at the head
            if position == 0:
                node = self.head
                node.prev = newNode
                newNode.next = node
                self.head = newNode
                self.size += 1

            # if inserting in the middle
            else:
                prevNode = node.prev
                newNode.prev = node.prev
                node.prev = newNode
                newNode.next = node
                prevNode.next = newNode
                self.size += 1

    # ------------------------------------------------------------------

    def pop(self, position=-1) -> Item:
        """
        removes and returns the item at the index specified by position; raises IndexError if position out of range
        :param position: index to remove at
        :return: value that was removed
        """

        # calls _delete to remove the node
        item = self._delete(position)
        # returns the item that was removed
        return item

    # ------------------------------------------------------------------

    def remove(self, x: Item):
        """
        removes the first value x from the list; raises ValueError if x is not in the list
        :param x: the value to remove from the list
        :return: None
        """

        inList = False
        # index accumulator
        index = -1

        # loops through each item in the list
        for i in self:
            index += 1

            # if the value is found, then inList is set to True
            # otherwise it stays false and raises a ValueError.
            if i == x:
                inList = True
                break

        if not inList:
            raise ValueError(f"The value {x} is not in the list")

        # calls the _delete method and passes through the index of the item
        self._delete(index)

    # ------------------------------------------------------------------

    def index(self, x: Item, start=0) -> int:
        """
        :param x: the value to find the index of
        :param start: the non-negative starting index to start searching for x
        :return: the non-negative index of the first copy of x at location start or later in the list
        """
        # index accumulator
        index = 0

        # retrieves the node at the head
        node = self.head

        # loops through each node in the list
        for i in range(self.size):

            if index > 0:
                node = node.next

            # if the item is found and the index is after or equal to the starting point
            if node.item == x and index >= start:
                # return the correct index
                return index

            # if it isn't found, increment index and loop again
            else:
                index += 1

        raise ValueError


    # ------------------------------------------------------------------

    def count(self, x: Item) -> int:
        """
        :param x: the value to count in the list
        :return: the number of copies of x in the list
        """
        # accumulator
        count = 0

        # loops through the items in the DList
        for i in self:

            # if a match is found, increment the count
            if i == x:
                count += 1

        # after looping through the whole DList, return the count
        return count

    # ------------------------------------------------------------------

    def extend(self, seq: Iterable):
        """
        adds each of the elements in seq to the end of the list
        :param seq: the iterable sequence to add its items on the list
        :return: None
        """
        # creates a new DList object
        new = DList()

        # loops through the seq and appends them to the new DList.
        # this is to prevent an infinite loop if extending an object with itself
        for i in seq:
            new.append(i)

        # appends each item in the new list to self
        for i in new:
            self.append(i)


    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
