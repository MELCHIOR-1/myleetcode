#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No46_permutations.py
@time: 4/6/17 11:07 PM
"""


class Solution(object):
    def __init__(self):
        pass

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permuteRecu(nums,0,result)
        return result

    def permuteRecu(self,nums,begin,result):
        if begin>=len(nums)-1:
            result.append(list(nums))
            return
        else:
            for i in range(begin,len(nums)):
                nums[begin],nums[i]=nums[i],nums[begin]
                self.permuteRecu(nums,begin+1,result)
                nums[begin], nums[i] = nums[i], nums[begin]

if __name__ == '__main__':
    print Solution().permute([1,2,3])