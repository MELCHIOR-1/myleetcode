# -*- coding: utf-8 -*-
"""
Created on Thu Mar  12 21:32:48 2017

@author: shawpan
"""
# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
#

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {'(':')','[':']','{':'}'}
        stack = []
        for i in range(len(s)):
            if len(stack)>0 and map.get(stack[-1]) == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0
if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")
