#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No38_Count and Say.py
@time: 3/26/17 12:03 AM
"""

# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.
#O(n2)
# 使用递归实现
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1: return '1'
        s = self.countAndSay(n-1)
        res = ''
        p = count = 0
        for i in range(len(s)):
            if s[p]==s[i]:
                count += 1
            else:
                res = res + str(count) + s[p]
                p, count = i, 1
        return res + str(count) + s[p]

if __name__ == '__main__':
    print Solution().countAndSay(1)
    print Solution().countAndSay(2)
    print Solution().countAndSay(3)
    print Solution().countAndSay(4)
    print Solution().countAndSay(5)
