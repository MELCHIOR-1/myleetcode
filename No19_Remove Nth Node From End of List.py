# -*- coding: utf-8 -*-
"""
Created on Thu Mar  12 21:32:48 2017

@author: shawpan
"""
# Time:  O(n)
# Space: O(1)
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.
#


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

# 此题为快慢指针问题
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return None
        fast, slow = head, head #初始化快慢指针
        i = 0
        while (fast.next):  # 看快指针的下一个是否为空
            if i >= n:    slow = slow.next  # 让快指针先走n步
            fast = fast.next
            i = i + 1
        if i < n: return head.next  # 这里主要考虑删除的是头指针的话，就要返回头指针下一个
        slow.next = (slow.next).next # 将要删除的节点的上一个节点的next指向要删除节点的next，这步要写在上步下面，因为头指针前面没有指针
        return head

# 这种方法比较好，对于所有情况都统一到一起
class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)    # 在头结点新建一个虚拟的节点
        dummy.next = head   # 是这个节点指向头结点
        slow, fast = dummy, dummy   # 把快慢指针都初始化到该节点
        for i in range(n): fast = fast.next # 让快节点先走n步
        while fast.next:
            slow, fast = slow.next, fast.next   # 使快指针遍历到链表尾，慢指针为要删除的节点的前一个节点
        slow.next = slow.next.next  # 删除指定节点
        return dummy.next   # 返回虚拟节点的下一个节点，这样的好处是避免讨论首节点是否被去除掉的问题


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().removeNthFromEnd(head, 2)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution1().removeNthFromEnd(head, 2)