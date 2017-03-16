# -*- coding: utf-8 -*-
"""
Created on Thu Mar  15 21:32:48 2017

@author: shawpan
"""

# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#
# Subscribe to see which companies asked this question.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

# 使用递归实现交换
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next): return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n

class Solution1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode(-1)
        pre.next = head
        while pre.next and pre.next.next:
            a,b = pre.next,pre.next.next
            pre.next,b.next,a.next = b,a,b.next
            pre = a
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().swapPairs(head)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution1().swapPairs(head)