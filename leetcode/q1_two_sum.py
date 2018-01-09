# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Time: O(n)
# Space: O(n)
#
# 给定一个整形数组和一个指定的数值，当数组中存在两个数的和等于目标数值，返回
# 这两个数的索引值(indices)
#
# 手动保证唯一结果
#
# Example:
# Given nums = [2, 7, 11, 15] target = 9,
# return [0, 1]
#
# 解决办法：
# 初始化一个字典dict,其key为nums中数的值，其value为数值对应的索引，
# 使用enumerate遍历数组，i为索引，num为数值，判断target - num是否在dict中(key)，
# 如果不存在，将{num, i}存入dict，
# 否则，返回target - num在dict中的value(即索引)和当前数值的索引

class Solution(object):

    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i


if __name__ == '__main__':
    print (Solution().twoSum((2, 7, 11, 15), 26))
