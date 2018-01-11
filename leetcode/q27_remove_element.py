# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Given an array and a value, remove all instances of that value in-place and return the new length
#
# 要求 space: O(1)
#
# Example:
# Given nums = [3, 2, 2, 3], val = 3
# return 2


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, last = 0, len(nums) - 1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return last + 1

if __name__ == "__main__":
    print(Solution().removeElement([1, 2, 3, 4, 5], 2))