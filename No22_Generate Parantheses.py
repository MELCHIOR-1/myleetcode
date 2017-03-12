# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:32:48 2017

@author: shawpan
"""
# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateParenthesisRecu(res,'',n,n)
        return  res

    # 这里相当于传递res的引用，比返回值传递好
    def generateParenthesisRecu(self,res,current,left,right):
        # 这几个判断很巧妙，注意是多个判断，会顺序执行。值得多看几遍。。
        if left == 0 and right == 0:
            res.append(current)
        if left > 0:
            self.generateParenthesisRecu(res,current+'(',left-1,right)
        if left < right:
            self.generateParenthesisRecu(res,current+')',left,right-1)

if __name__ == "__main__":
    print Solution().generateParenthesis(3)