# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
# Example:
# Input: haystack = "hello" , needle = "ll"
# output: 2


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 把needle看成一个整体
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    def strStr2(self, haystack, needle):
        return haystack.find(needle)

if __name__ == "__main__":
    print(Solution().strStr2("a", ""))
    print(Solution().strStr2("hello", "ll"))