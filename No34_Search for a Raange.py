# -*- coding: utf-8 -*-
"""
Created on Thu Mar  19 21:32:48 2017

@author: shawpan
"""
# Given an array of integers sorted in ascending order, find the
#
# starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,

# Given [5, 7, 7, 8, 8, 10] and target value 8,

# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start,stop = -1,-1
        for i in range(len(nums)):
            if nums[i]==target:
                if not (start>=0 and nums[start]==target):
                    start = i
                stop = i
        return [start,stop]
if __name__ == "__main__":
    print Solution().searchRange([5,7,7,8,8,9],8)
