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

# getItem Tests
# ------------------------------------------------------------------

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

# setItem Tests
# ----------------------------------------------------------------------

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


    # delItem Tests
# ----------------------------------------------------------------------

    def testDeleteItem(self):

        items = DList()

        # Checks to make sure IndexError is raised.
        with self.assertRaises(IndexError):
            items[6] = 20

        items.extend([4, 6, 7, 2, 1, 7, 0])

        # Checks it returns the correct item
        del items[3]
        self.assertEqual(items[3], 1)
        del items[-5]
        self.assertEqual(items[-5], 2)
        self.assertEqual(items[5], 8)
        self.assertEqual(items[2], 5)



# clear() Tests
# ----------------------------------------------------------------------

# insert() Tests
# ----------------------------------------------------------------------

# pop() Tests
# ----------------------------------------------------------------------

# remove() Tests
# ----------------------------------------------------------------------

# index() Tests
# ----------------------------------------------------------------------

# count() Tests
# ----------------------------------------------------------------------

# extend() Tests
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