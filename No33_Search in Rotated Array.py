# -*- coding: utf-8 -*-
"""
Created on Thu Mar  19 21:32:48 2017

@author: shawpan
"""

# Suppose an array sorted in ascending order is rotated at some
#
# pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array
#
# return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo,hi = 0,n-1
        while(lo<hi):
            mid = (lo+hi)/2
            if nums[mid]>nums[hi]:  # 注意这步比较的项
                lo = mid + 1
            else:
                hi = mid
        rot = lo
        # print rot,mid
        lo, hi = 0,n-1
        while(lo<=hi):
            mid = (lo+hi)/2
            realMid = (mid + rot) % n
            # print mid,realMid
            if nums[realMid] == target: return realMid
            elif nums[realMid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

if __name__ == "__main__":
    print Solution().search([3,1],1)
    print Solution().search([1,3], 1)

