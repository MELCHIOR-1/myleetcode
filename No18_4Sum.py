# -*- coding: utf-8 -*-
"""
Created on Thu Mar  12 21:32:48 2017

@author: shawpan
"""


# Given an array S of n integers,
# are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
#   A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)
#
# Time:  O(n^2 * p) ~ O(n^4)
# Space: O(n^2)

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import collections
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                lookup[nums[i]+nums[j]].append([i,j])   # 将数字两两分组，之和存在key中，这两个数存在值中

        for i in lookup.keys():     # 将4个数之和转换成两个数之和，然后再找这两个数对应的4个数的情况
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target-i]:
                        [a, b],[c, d] = x, y
                        if (a not in [c,d]) and (b not in [c,d]):
                            quad = sorted([nums[a],nums[b],nums[c],nums[d]])
                            if quad not in result:
                                result.append(quad)

        return sorted(result)

if __name__ == '__main__':
    result = Solution().fourSum([1,0,-1,0,-2,2],0)
    print result