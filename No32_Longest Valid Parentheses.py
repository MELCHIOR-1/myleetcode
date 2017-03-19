# -*- coding: utf-8 -*-
"""
Created on Thu Mar  19 21:32:48 2017

@author: shawpan
"""


# Given a string containing just the characters '(' and ')',
#
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has
# length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring
#
# is "()()", which has length = 4.

class Solution(object):
    # DP: 用一个longestList数组的索引对应原数组的索引，其值存储以s[i]结尾的最长匹配的值
    # 如：s = ["()(())"],longestList = [0,2,0,0,2,6]
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestList = []
        maxLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                longestList.append(0)
            else:
                if i>=1 and s[i-1] == '(':
                    longestList.append(longestList[i-2]+2 if i>=2 else 2)
                else:
                    if i>=1 and i-longestList[i-1]-1>=0 and s[i-longestList[i-1]-1] == '(':
                        longestList.append(longestList[i-1]+2+(longestList[i-longestList[i-1]-2] if i-longestList[i-1]-2>=0 else 0))
                    else:
                        longestList.append(0)
            maxLen = max(maxLen, longestList[i])
            # print longestList
        return maxLen



if __name__ == "__main__":
    print Solution().longestValidParentheses("()(()")
    print Solution().longestValidParentheses("()()")
    print Solution().longestValidParentheses("()(())")
    print Solution().longestValidParentheses(")(")
    print Solution().longestValidParentheses("(()()")
