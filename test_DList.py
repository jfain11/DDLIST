#!/usr/bin/env python3

# ----------------------------------------------------------------------
# test_DList.py
# Dave Reed
# 05/14/2021

# ----------------------------------------------------------------------
import copy
import sys
import unittest

sys.path.insert(0, '..')
from DList import *


# ----------------------------------------------------------------------

class DListTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def checkList(self, linked: DList, seq: list):

        self.assertEqual(len(linked), len(seq))
        items = list(linked)
        self.assertEqual(items, seq, f"DList: {items} != {seq}")
        revSeq = list(reversed(seq))
        revItems = []
        node = linked.tail
        while node is not None:
            revItems.append(node.item)
            node = node.prev
        self.assertEqual(revItems, revSeq, f"DList reversed via prev links: {revItems} != {revItems}")

        if len(seq) > 0:
            self.assertIsNone(linked.head.prev, "head.prev is not None")
            self.assertEqual(linked.head.item, seq[0], "head is not correct")
            self.assertEqual(linked.tail.item, seq[-1], "tail is not correct")
            self.assertIsNone(linked.tail.next, "tail.next is not None")
        else:
            self.assertIsNone(linked.head, "empty list, head is not None")
            self.assertIsNone(linked.tail, "empty list, tail is not None")

    # ------------------------------------------------------------------

    def testAppendMultiple(self):
        items = DList()
        for x in range(2, 6):
            items.append(x)
        self.checkList(items, [2, 3, 4, 5])

# ------------------------------------------------------------------

# getItem Tests

    def testGetItemRaisesIndexError(self):

        items = DList()

        # Checks to make sure IndexError is raised.
        with self.assertRaises(IndexError):
            x = items[0]

        items.extend([2,4,5,6,7,8])

        # Checks it returns the correct item
        self.assertEqual(items[-2], 7)
        self.assertEqual(items[0], 2)
        self.assertEqual(items[5], 8)
        self.assertEqual(items[2], 5)

#----------------------------------------------------------------------

# setItem Tests

    def testSetItem(self):

        items = DList()

        # Checks to make sure IndexError is raised.
        with self.assertRaises(IndexError):
            items[6] = 20

        items.extend([2, 4, 5, 6, 7, 8])

        # Checks the items are set correctly
        items[-2] = 3
        self.assertEqual(items[-2], 3)
        items[0] = 5
        self.assertEqual(items[0], 5)
        items[5] = 2
        self.assertEqual(items[5], 2)
        items[2] = 9
        self.assertEqual(items[2], 9)

# ----------------------------------------------------------------------
    # delItem Tests

    def testDeleteItem(self):

        items = DList()

        # Checks to make sure IndexError is raised.
        with self.assertRaises(IndexError):
            items[6] = 20

        items.extend([4, 6, 7, 2, 1, 7, 0])

        # Checks the item is successfully deleted
        del items[-7]
        del items[5]
        del items[2]
        del items[0]
        del items[-1]

        self.checkList(items, [7, 1])

# ----------------------------------------------------------------------

# clear() Tests

    def testClear(self):

        items = DList()
        items.extend([8, 4, 2, 4, 1, 6, 8])

        items.clear()

        self.checkList(items, [])

# ----------------------------------------------------------------------

# insert() Tests

    def testInsert(self):
        items = DList()
        items.insert(2, 1)
        self.checkList(items, [1])
        items.insert(0, 2)
        self.checkList(items, [2, 1])
        items.insert(-4, 3)
        self.checkList(items, [3, 2, 1])
        items.insert(1, 9)
        self.checkList(items, [3, 9, 2, 1])
        items.insert(10, 5)
        self.checkList(items, [3, 9, 2, 1, 5])


# ----------------------------------------------------------------------

# pop() Tests

    def testPop(self):
        items = DList()
        items.extend([4, 5, 9, 1, 8, 0, 3])

        a = items.pop(0)
        self.checkList(items, [5, 9, 1, 8, 0, 3])
        self.assertEqual(a, 4)

        b = items.pop(5)
        self.checkList(items, [5, 9, 1, 8, 0])
        self.assertEqual(b, 3)

        c = items.pop(2)
        self.checkList(items, [5, 9, 8, 0])
        self.assertEqual(c, 1)

        d = items.pop(-1)
        self.checkList(items, [5, 9, 8])
        self.assertEqual(d, 0)

        with self.assertRaises(IndexError):
            e = items.pop(10)

        with self.assertRaises(IndexError):
            e = items.pop(-9)

# ----------------------------------------------------------------------

# remove() Tests

    def testRemove(self):
        items = DList()
        items.extend([9, 4, 8, 3, 2, 6, 7])

        items.remove(9)
        self.checkList(items, [4, 8, 3, 2, 6, 7])

        items.remove(2)
        self.checkList(items, [4, 8, 3, 6, 7])

        items.remove(7)
        self.checkList(items, [4, 8, 3, 6])

        with self.assertRaises(ValueError):
            items.remove(1)

        with self.assertRaises(ValueError):
            items.remove(20)

# ----------------------------------------------------------------------

# index() Tests

    def testIndex(self):
        items = DList()
        items.extend([9, 3, 1, 0, 14, 7, 3])

        index = items.index(9)
        self.assertEqual(index, 0)

        index = items.index(3)
        self.assertEqual(index, 1)

        index = items.index(3, 5)
        self.assertEqual(index, 6)

        index = items.index(14)
        self.assertEqual(index, 4)

        with self.assertRaises(ValueError):
            index = items.index(21)

# ----------------------------------------------------------------------

# count() Tests

    def testCount(self):
        items = DList()
        items.extend([9, 2, 5, 1, 9, 9, 2, 14, 7, 0])

        a = items.count(9)
        self.assertEqual(a, 3)

        a = items.count(2)
        self.assertEqual(a, 2)

        a = items.count(0)
        self.assertEqual(a, 1)

        a = items.count(4)
        self.assertEqual(a, 0)

# ----------------------------------------------------------------------

# extend() Tests

    def testExtend(self):
        items = DList()
        items.extend([8, 1, 4, 6])
        self.checkList(items, [8, 1, 4, 6])

        items.extend(items)
        self.checkList(items, [8, 1, 4, 6, 8, 1, 4, 6])

        items.clear()

        items.extend([5])
        items.extend((3, 3, 1, 4))
        self.checkList(items, [5, 3, 3, 1, 4])
# ----------------------------------------------------------------------


def main():
    try:
        unittest.main()
    except SystemExit as inst:
        # raised by sys.exit(True) when tests failed
        if inst.args[0] is True:
            raise


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()