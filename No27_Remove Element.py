# -*- coding: utf-8 -*-
"""
Created on Thu Mar  16 21:32:48 2017

@author: shawpan
"""
#
# Given an array and a value, remove all instances of that value in
#
# place and return the new length.
#
# Do not allocate extra space for another array, you must do this
#
# in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you
#
# leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements
#
# of nums being 2.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        if len(nums)==1 and nums[0]==val: return 0
        i,j = 0,0
        while(j<len(nums)):

            if i == j: j = j + 1
            while (j<len(nums) and nums[j] == val): j = j + 1
            if j == len(nums) and nums[i]==val: break
            if(nums[i]==val):
                nums[i]=nums[j]
                nums[j]=val
            i = i+1
        return i

if __name__ == "__main__":
    nums  = [3,2,2,3,4]
    a = Solution().removeElement(nums,3)
    print a,nums
