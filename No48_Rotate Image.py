#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No48_Rotate Image.py
@time: 4/7/17 12:30 AM
"""


class Solution(object):
    def __init__(self):
        pass

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list,zip(*matrix[::-1]))

if __name__ == '__main__':
    pass