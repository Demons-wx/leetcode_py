# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Given a sorted array, remove the duplicates in-place such that each element
# appear only once and return the new length.
#
# 不允许开辟额外的数组空间，额外空间控制在O(1)

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        last, i = 0, 1 # last用来记录不同数字的个数，i用来遍历数组
        while i < len(nums):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i] # nums[last] 用来存储当前用来比较的数字
            i += 1
        return last + 1

if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2, 2]))