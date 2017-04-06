#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No47_Permutations II.py
@time: 4/6/17 11:20 PM
"""

# Status: Time Limit Exceeded

class Solution(object):
    def __init__(self):
        pass

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.permuteRecu(nums, 0, result)
        return result

    def permuteRecu(self, nums, begin, result):
        if begin >= len(nums) - 1:
            if not nums in result:
                result.append(list(nums))
            return
        else:
            for i in range(begin, len(nums)):
                if nums[begin]==nums[i] and begin != i:
                    continue
                nums[begin], nums[i] = nums[i], nums[begin]
                self.permuteRecu(nums, begin + 1, result)
                nums[begin], nums[i] = nums[i], nums[begin]

if __name__ == '__main__':
    print Solution().permuteUnique([1,1,2,2])