# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:32:48 2017

@author: shawpan
"""

# Time:  O(n)
# Space: O(1)
#
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below
# and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that
# form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#
class Solution(object):
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        if len(str1) == 0: return 0 # 如果字符串为空，则返回0
        str2 = str1.strip() # 去掉字符串两边的空格
        if len(str2) == 0: return 0 # 如果去掉空格后，字符串为空，说明字符串只有空格，返回0
        flag = 0    # 使用一个标志来记录‘+’，‘-’
        if str2[0] == '+':
            if len(str2) > 1:
                num = self.convert(str2[1:])    # 对字符串转换成数字
                return num if num < 2147483647 else 2147483647  #如果数字越界，则返回边界值
            else:
                return 0    # 说明字符串只含‘+’号

        elif str2[0] == '-':
            if len(str2) > 1:
                num = self.convert(str2[1:])
                return -num if num < 2147483648 else -2147483648
            else:
                return 0
        else:
            num = self.convert(str2)
            return num if num < 2147483647 else 2147483647

    def convert(self, positive_str):
        tempList = []   # 现将字符串中含数字的字符保存到list中
        i = 0
        while i < len(positive_str) and positive_str[i] >= '0' and positive_str[i] <= '9':
            tempList.append(positive_str[i])
            i = i + 1
        if len(tempList) == 0:
            return 0
        else:
            return int(''.join(tempList))   # 将list转换成string，然后int（）函数转换成整数

# 这种方法要更好一些
class Solution1(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = 0

        if not str:
            return result   # 如果字符串为空，返回0

        i = 0
        while i < len(str) and str[i] == " ": # 寻找前面的空格，指针跳过这些空格
            i += 1

        sign = 1    # 设置一个符号标志
        if str[i] == "+":   # ‘+’，指针加1
            i += 1
        elif str[i] == "-": # ‘-’，指针加1，并将符号标志设为-1
            sign = -1
            i += 1

        while i < len(str) and str[i] >= '0' and str[i] <= '9': # 判断字符是否是数字字符
            if result > (INT_MAX - (ord(str[i]) - ord('0'))) / 10: # Python自带的ord()函数，返回字符的ASCII码，判断转换后是否会越界
                return INT_MAX if sign > 0 else INT_MIN # 判断是越上界还是下界
            result = result * 10 + ord(str[i]) - ord('0') # 原数乘10，加上当前数字
            i += 1

        return sign * result


if __name__ == "__main__":
    print Solution().myAtoi("")
    print Solution().myAtoi("-1")
    print Solution().myAtoi("2147483647")
    print Solution().myAtoi("2147483648")
    print Solution().myAtoi("-2147483648")
    print Solution().myAtoi("-2147483649")
    print Solution1().myAtoi("")
    print Solution1().myAtoi("-1")
    print Solution1().myAtoi("2147483647")
    print Solution1().myAtoi("2147483648")
    print Solution1().myAtoi("-2147483648")
    print Solution1().myAtoi("-2147483649")