# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# 给定一个罗马数字，将其转换为整数，输入保证在1~3999范围内
# 规则：
# 1. 相同的数字连写，表示的数等于这些数字相加得到的数，如XXX表示30
# 2. 小的数字在大的数字右边，所表示的数等于这些数字相加得到的数，如VIII表示8
# 3. 小的数字在大的数字左边，所表示的数等于大数减去小的数：如IV表示4
# 4. 在一个数的上面画一条横线，便是这个数增值1000倍

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i-1]]:
                # 小的数字在大的数字左边，这两个数字将合并表示一个数字，所以减去2倍的小的数字
                # 表示将前面循环加上的小的数字减去
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]

        return decimal

if __name__ == "__main__":
    print(Solution().romanToInt("IIVX"))
    print(Solution().romanToInt("MMMCMXCIX")) # 3999