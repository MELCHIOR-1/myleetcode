# -*- coding: utf-8 -*-
"""
Created on Thu Mar  17 21:32:48 2017

@author: shawpan
"""

# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

# Time:O(logn)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0: return -2147483648 if dividend<0 else 2147483647
        positive = (dividend > 0) is (divisor>0) #判断是否除数和被除数是否相等
        dividend,divisor = abs(dividend),abs(divisor) # 转化为正数
        res = 0
        while(dividend>=divisor):
            temp,i = divisor,1
            while(dividend>=temp):  # 将除数两倍增长，以加快相减的速度
                dividend -= temp
                res += i
                # print i,dividend
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648,res),2147483647) # 定界，这个写法很简洁

if __name__ == "__main__":
    a = Solution().divide(2,0)
    print a