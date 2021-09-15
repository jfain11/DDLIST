#!/usr/bin/env python3

# ----------------------------------------------------------------------
# DListNode.py
# Dave Reed
# 05/14/2021
# ----------------------------------------------------------------------

from __future__ import annotations

from typing import Optional
from typing import Union

Item = Union[int, float, str]


class DListNode:

    """data value along with previous and next links"""

    item: Item
    prev: Optional[DListNode]
    next: Optional[DListNode]


    # ------------------------------------------------------------------

    def __init__(self, item: Item, prev: Optional[DListNode] = None, next: Optional[DListNode] = None):
        """
        :param item: value to store in the node
        :param prev: link to previous node
        :param next: link to next node
        """
        self.item = item
        self.prev = prev
        self.next = next

    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
