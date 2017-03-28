# -*- coding: utf-8 -*-
"""
Created on Thu Mar  19 21:32:48 2017

@author: shawpan
"""
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled
#
#  with the character '.'.
#
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
#
# Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 行扫描
        for i in range(9):
            if not self.isValid(board[i]): return False
        # 列扫描
        for i in range(9):
            if not self.isValid([x[i] for x in board]): return False
        # 九宫格扫描
        for i in range(3):
            for j in range(3):
                if not self.isValid(reduce(lambda x,y:x+y,[x[i*3:(i+1)*3] for x in board[j*3:(j+1)*3]])): return False
        return True

    def isValid(self,nums):
        temp = [0,0,0,0,0,0,0,0,0]
        for i in range(len(temp)):
            if nums[i] != '.':
                if temp[int(nums[i])-1] != 0:
                    return False
                else:
                    temp[int(nums[i])-1] = int(nums[i])
        return True
if __name__ == "__main__":
    print Solution().isValidSudoku([[  5,  3,'.','.',  7,'.','.','.','.'],\
                                    [  6,'.','.',  1,  9,  5,'.','.','.'],\
                                    ['.',  9,  8,'.','.','.','.',  6,'.'],\
                                    [  8,'.','.','.',  6,'.','.','.',  3],\
                                    [  4,'.','.',  8,'.',  3,'.','.',  1],\
                                    [  7,'.','.','.',  2,'.','.','.',  6],\
                                    ['.',  6,'.','.','.','.',  2,  8,'.'],\
                                    ['.','.','.',  4,  1,  9,'.','.',  5],\
                                    ['.','.','.','.',  8,'.','.',  7,  9]])