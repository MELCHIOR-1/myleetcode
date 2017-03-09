# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:32:48 2017

@author: shawpan
"""

# Time:  O(n)
# Space: O(1)
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the xrange from 1 to 3999.
#

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 主要思路是对字符串进行挨个扫描，可以看出,，罗马字符转十进制基本上就是把字符对应的数字相加，如III（3），可以看成1+1+1；但是有些特殊情况需要考虑，如4,40,400对应的罗马数字
        roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # 建立罗马数字到十进制数的映射表
        decimal = 0
        for i in range(len(s)):
            factor = 1
            if i < len(s)-1:
                factor = -1 if roman_map[s[i]] < roman_map[s[i+1]] else 1 # 比较当前字符和下一个字符，如果下一个字符比当前字符大，说明为×4（IV）的情况，可以看成是5-1,使用factor保存这个信息
            decimal = decimal + factor * roman_map[s[i]]
        return decimal


if __name__ == "__main__":
    print Solution().romanToInt("IIVX")
    print Solution().romanToInt("MMMCMXCIX")