# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Reverse digits of an integer
#
# Example1: x = 123 return 321
# Example2: x = -123 return -321
# Example3: x = 1230 return 321
#
# 注意整数越界


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result if result <= 0x7fffffff else 0


    # 使用python切片操作
    def reverse2(self, x):
        if x < 0:
            # str(x)[::-1][-1] 表示将str(x)倒序输出并取出最后一位(即 - ),
            # str(x)[::-1][:-1] 表示将str(x)倒叙输出并取[0:-1]位
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1]) # -1 表示每隔1个取1个从最后一个开始
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x

if __name__ == "__main__":
    print(Solution().reverse2(-1230))
