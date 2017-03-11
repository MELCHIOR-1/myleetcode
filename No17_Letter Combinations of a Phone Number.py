# -*- coding: utf-8 -*-
"""
Created on Thu Mar  10 21:32:48 2017

@author: shawpan
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_map = ['0', '1', 'abc', 'def', 'ghi','jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if not len(digits): return []
        dgt = [int(x) for x in list(digits)]
        temp = [list(phone_map[x]) for x in dgt]
        result = ['']
        for i in range(len(temp)):
            result = [x+y for x in result for y in temp[i]]
        return result

if __name__ == "__main__":
    print Solution().letterCombinations('234')
