# -*- coding: utf-8 -*-
"""
Created on Thu Mar  10 21:32:48 2017

@author: shawpan
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return 0
        nums.sort()
        min_error = sum(nums[0:3]) - target
        for i in range(len(nums)-1):

            j = i +1
            k = len(nums)-1
            while(j<k):
                error = nums[i] + nums[j] + nums[k] -target
                if error < 0:
                    j = j+1
                else:
                    k = k-1
                min_error = min_error if abs(min_error) < abs(error) else error

        return min_error + target

if __name__ == "__main__":
    print Solution().threeSumClosest([-1, 2, 1, -4],1)