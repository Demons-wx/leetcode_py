# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Given a sorted array and a target value, return the index if the
# target is found. if not, return the index where it would be if it were inserted in order.
#
# assume no duplicates in the array
#
# Example:
# Input: [1, 3, 5, 6], 5
# Output: 2
# Input: [1, 3, 5, 6], 2
# Output: 1



class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return i + 1

if __name__ == '__main__':
    print (Solution().searchInsert((2, 7, 11, 15), 26))
