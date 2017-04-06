#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No50_Pow.py
@time: 4/7/17 12:35 AM
"""


class Solution(object):
    def __init__(self):
        pass
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==-1:
            return 1.0/x
        m = n//2
        temp = self.myPow(x,m)
        if n % 2:
            return x * temp * temp
        else:
            return temp * temp


if __name__ == '__main__':
    print Solution().myPow(4,3)