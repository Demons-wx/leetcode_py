# -*- coding: utf-8 -*-  
__author__ = "wangxuan"


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
#
# Time: O(n)


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese) # 如果是 左半边 括号，压入栈中
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese: # 如果是右半边括号，从栈中弹出一个看是否匹配
                return False

        return len(stack) == 0

if __name__ == "__main__":
    print(Solution().isValid("([])"))