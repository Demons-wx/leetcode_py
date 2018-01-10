# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# find the longest common prefix string amongst an array of strings
# 最长公共前缀
#
# Time: O(n*k) k是公共前缀的长度

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])): # 遍历第一个字符串
            for string in strs[1:]: # 从第二个字符串开始比较
                if i >= len(string) or string[i] != strs[0][i]: # 当第i个字符不等于其他字符串中同位置的字符时
                    return strs[0][:i] # 返回第一个字符串的前i-1个字符

        return strs[0]

    def longestCommonPrefix2(self, strs):
        if len(strs) == 0:
            return ''

        pre = strs[0]
        for st in strs[1:]:
            while 1:
                if st.startswith(pre):
                    break
                else:
                    pre = pre[:-1]
        return pre

if __name__ == "__main__":
    print(Solution().longestCommonPrefix2(["hello", "heaven", "heavy"]))