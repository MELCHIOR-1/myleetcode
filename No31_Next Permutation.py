# -*- coding: utf-8 -*-
"""
Created on Thu Mar  16 21:32:48 2017

@author: shawpan
"""

# Implement next permutation, which rearranges numbers into the
#
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as
#
# the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and
#
# its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k, l = -1, 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                k = i

        if k == -1:
            nums.reverse()
            return

        for i in range(k + 1, len(nums)):
            if nums[i] > nums[k]:
                l = i

        nums[k], nums[l] = nums[l], nums[k] #交换k,l位置的值
        nums[k + 1:] = nums[:k:-1]  # 将k+1至结尾的数列翻转

if __name__ == "__main__":
    nums  = [1,4,3,2]
    Solution().nextPermutation(nums)
    print nums