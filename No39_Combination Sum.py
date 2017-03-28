#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No39_Combination Sum.py
@time: 3/26/17 1:09 AM
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result,temp = [],[]
        self.combinationSumRecu(sorted(candidates),result,0,temp,target)
        return result

    def combinationSumRecu(self, candidates, result, start, temp, target):
        if target == 0:
            print type(temp),temp,result
            result.append(list(temp)) # 注意此处不能直接append(temp)，否则是浅拷贝，之后temp.pop()时会将result中的数也pop出来
        while start < len(candidates) and candidates[start]<=target:
            temp.append(candidates[start])
            self.combinationSumRecu(candidates, result, start, temp,target-candidates[start])
            temp.pop()
            start += 1

if __name__ == '__main__':
    print Solution().combinationSum([2,3,6,7],7)