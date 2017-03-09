# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:00:18 2017

@author: shawpan
"""

# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

# Write a function to find the longest common prefix string
# amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in xrange(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]: # 当索引大于等于任意一个字符串的长度，或者字符不相等时，停止查找
                    return strs[0][:i]
        return strs[0]


class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        if len(strs)==0:
            return ''
        strs.sort() # 先对字符串排序，然后只需要比较第一个和最后一个字符串就行，这两个差异最大
        p = strs[0]
        q = strs[len(strs)-1]
        prefix = ''
        i = 0
        while(i<len(p) and i<len(q) and p[i]==q[i]):
            prefix = prefix + p[i]
            i=i+1
        return prefix


if __name__ == "__main__":
    print Solution().longestCommonPrefix(["hello", "heaven", "heavy"])
    print Solution1().longestCommonPrefix(["hello", "heaven", "heavy"])