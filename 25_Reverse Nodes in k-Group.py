# -*- coding: utf-8 -*-
"""
Created on Thu Mar  15 21:32:48 2017

@author: shawpan
"""

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head = self.reverseFirstK(head, k)
        if k == 1: return head
        p = ListNode(-1)
        p.next = head
        for i in range(k):
            p = p.next
            if not p:
                return head
        tail = p
        tail.next = self.reverseKGroup(tail.next,k)
        return head

    def reverseFirstK(self,head,k):
        if k == 1 or head == None: return head
        p = ListNode(-1)
        p.next = head
        for i in range(k):
            p = p.next
            if not p:
                return head
            # print k,p
        n = head.next
        head.next = p.next
        p.next = head
        head = self.reverseFirstK(n,k-1)
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print Solution().reverseKGroup(head,2)