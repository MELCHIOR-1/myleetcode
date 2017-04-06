#! /usr/bin/env python
#coding=utf-8

"""
@version: ??
@author: shawpan
@license: Apache Licence 
@contact: shawpan@yeah.net
@software: PyCharm
@file: No40_Combination Sum II.py
@time: 3/29/17 12:51 AM
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result, temp = [], []
        self.combinationSumRecu(sorted(candidates), result, 0, temp, target)
        return result

    def combinationSumRecu(self, candidates, result, start, temp, target):
        if target == 0:
            if temp not in result:
                result.append(list(temp))  # 注意此处不能直接append(temp)，否则是浅拷贝，之后temp.pop()时会将result中的数也pop出来
        while start < len(candidates) and candidates[start] <= target:
            temp.append(candidates[start])
            self.combinationSumRecu([candidates[i] for i in range(len(candidates)) if i != start], result, start, temp, target - candidates[start])
            temp.pop()
            start += 1


if __name__ == '__main__':
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)