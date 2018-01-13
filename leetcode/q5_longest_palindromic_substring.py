# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 最长回文子串
#
# Example:
# Input: "babad"
# Output: "bab"
#
# 长度为奇数的回文串以最中间的字符的位置为对称轴左右对称，而长度为偶数的回文串对称轴在
# 中间两个字符之间的间隙。可以利用这种对称性来提高算法效率
#
# 我们知道整个字符串中的所有字符，以及字符间的空隙，都可能是某个回文子串的对称轴位置，可以
# 遍历这些位置，在每个位置上同时向左和向右扩展，直到左右两边的字符不同，或者达到边界。


class Solution:

    def __init__(self):
        self.lo = 0
        self.maxLen = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def extendPalindrome(s, j, k):

            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            if self.maxLen < k - j - 1:
                self.lo = j + 1
                self.maxLen = k -j - 1

        if len(s) < 2:
            return s

        i = 0
        while i < len(s) - 1:
            extendPalindrome(s, i, i)
            extendPalindrome(s, i, i + 1)
            i += 1

        return s[self.lo:self.lo + self.maxLen]


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
