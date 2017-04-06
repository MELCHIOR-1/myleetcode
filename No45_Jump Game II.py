#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No45_Jump Game II.py
@time: 4/6/17 9:47 PM
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        edge, step ,maxReach= 0, 0, nums[0]
        for i in range(1,len(nums)):
            if edge < i:
                edge = maxReach
                step += 1
                if edge>=len(nums)-1:
                    return step
            maxReach = max(maxReach,i+nums[i])
            # print maxReach
            if maxReach == i:
                return -1
        return step

if __name__ == '__main__':
    print Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0])