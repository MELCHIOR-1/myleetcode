# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:32:48 2017

@author: shawpan
"""
# Time:  O(1)
# Space: O(1)
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#

# 使用一个变量记录回文数下部分的翻转值，然后将回文数变为其上部分，比较这两个数
# 这样的好处有2点：
# 1、比起整个数翻转，这个的迭代次数减半
# 2、变量的长度是x的一般，所以不会出现将x翻转后溢出的情况
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x>0 and x%10==0):    # 负数和个位为0的数都不可能为回文数
            return False
        else:
            sum = 0
            while(x>sum):
                sum = sum*10 + x%10     # 将回文数分成上部分和下部分，利用sum记录回文数下部分的翻转值
                x = x//10   # 将回文数一直除10，知道只剩上部分
            return (x==sum) or (x==sum//10) # 回文数分为位数为奇数和位数为偶数的情况，如12321，经过上面的步骤，sum=123，x=12；而123321，经过上面的步骤，sum=123，x=123


if __name__ == "__main__":
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(12320)
    print Solution().isPalindrome(-12321)