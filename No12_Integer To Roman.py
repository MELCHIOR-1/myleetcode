# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:32:48 2017

@author: shawpan
"""

# Time:  O(n)
# Space: O(1)
#
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 建立十进制和罗马字符的映射表，表为一个包含4个list的list，分别为个位、十位、百位、千位的映射。
        # 注意： 0 对应的罗马字符为空字符串
        romanCharList = [['','I','II','III','IV','V','VI','VII','VIII','IX']\
                        ,['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']\
                        ,['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']\
                        ,['','M','MM','MMM']]
        romanStr = ''
        i = 0
        while True:
            romanStr = romanCharList[i][num%10] + romanStr
            num = num //10
            if num  == 0:
                break
            else:
                i=i+1
        return romanStr


class Solution1:
    # @return a string
    def intToRoman(self, num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
                       500: "D", 900: "CM", 1000: "M"}
        keyset, result = sorted(numeral_map.keys()), ""

        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += numeral_map[key]

        return result


if __name__ == "__main__":
    print Solution().intToRoman(999)
    print Solution().intToRoman(3999)
    print Solution1().intToRoman(999)
    print Solution1().intToRoman(3999)