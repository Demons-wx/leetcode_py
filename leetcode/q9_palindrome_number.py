# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Determine whether an integer is a palindrome, Do this without extra space

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and x == int(str(x)[::-1]):
            return True
        else:
            return False

if __name__ == "__main__":
    print(Solution().isPalindrome(0))