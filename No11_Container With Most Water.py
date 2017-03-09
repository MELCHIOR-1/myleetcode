# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:32:48 2017

@author: shawpan
"""


# Time:  O(n)
# Space: O(1)
#
# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of
# line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container,
# such that the container contains the most water.
#
# Note: You may not slant the container.
#
# 这题使用最优化方法解决，实质上是个最优路径的问题
class Solution:
    # @return an integer
    def maxArea(self, height):
        max_area, i, j = 0, 0, len(height) - 1 # 使用两个指针，一个指向第一个元素，然后往后走；一个在指向最后一个元素，然后往前走
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i)) # 这里求最大面积值，面积=底X高，首先从间隔最大的值开始，两边较小者决定了高，这两个之间的元素与较小者组成的面积一定比两边组成的面积小，所以跳过这些情况
            if height[i] < height[j]:
                i += 1 # i与j组成的面积是i与ij之间的其他元素组成的面积大，所以i剩余的情况不用考虑，接着查找i+1
            else:
                j -= 1
        return max_area


if __name__ == "__main__":
    height = [1, 2, 3, 4, 3, 2, 1, 5]
    result = Solution().maxArea(height)
    print result