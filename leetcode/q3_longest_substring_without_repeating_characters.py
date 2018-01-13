# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Given a string, find the length of the longest substring without repeating characters.
#
# Note that the answer must be a substring not a subsequence
#
# Time: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # longest用来记录最长子串的长度
        # start作为子串中的遍历因子
        # 初始化一个全是False的ASCII码长度的visited数组，遍历字符串s，当ord(char)不在visited中时，置visited[ord(char)]为True
        # longest和start的变化比较难处理
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest


    def lengthOfLongestSubstring2(self, s):
        res = prev = i = 0
        dic = {}
        for x in s:
            if x in dic and dic[x] >= prev:
                res = max(i - prev, res)
                prev = dic[x] + 1
            dic[x] = i
            i += 1
        return max(i - prev, res)

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring2("pwwkew"))
