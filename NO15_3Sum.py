# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:25:32 2017

@author: shawpan
"""
# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3: return []
        result = []
        nums.sort() #先对数组按照从小到大的顺序进行排序，方便查找
        i = 0
        while(i<len(nums)-1):
            target = -nums[i] # 3个之和为0，则第一个数和后两个数互为相反数
            front = i+1 # 从第一个数的下一个数开始向后查找第二个数
            back = len(nums)-1 # 从数组最后开始向前查找第三个数
            while(front<back):
                twoSum = nums[front]+nums[back] # 计算后两个数之和
                if twoSum > target: #如果后两个数之和大于第一个数的相反数，说明第三个数取大了，因为第二个数是剩余数组里面最小的数
                    back = back -1 # 指向第三个数的指针往前移
                elif twoSum < target: # 说明第二个数小了，需要往后移
                    front = front + 1
                else:
                    temp = [nums[i],nums[front],nums[back]] # 将满足三个数之和为零的数存成一个数组
                    result.append(temp) # 存到需要返回的数组中
                    while(front < back and nums[front]==temp[1]): front = front + 1 # 如果第二个数的下一个数和第二个数一样，说明它和第一个、第三个数的和也为0，也满足条件，但是数组返回的数组中已经存在，所以要忽略这个数组，最好的办法就是指针直接跳过去
                    while(front < back and nums[back]==temp[2]): back = back -1 # 如果第三个的上一个和第三个数一样，说明也有重复，指针需要跳过去
            while(i<len(nums)-1 and nums[i]==nums[i+1]): i = i+1 # 如果第一个数的下一个和第一个数一样，则它的所有情况都包含在第一个数中，所以也需要跳过去
            i = i +1
        return result

if __name__ == '__main__':
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print result