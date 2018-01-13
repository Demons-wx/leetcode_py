# -*- coding: utf-8 -*-  
__author__ = "wangxuan"


# 給定n個非負的整數a1, a2,...,an, 坐標(i, ai) , (i, 0)
# 鏈接(i, ai)和(i, 0)畫直綫，共有n条，找出两条直线，使得两条直线与x轴形成
# 的容器能够盛更多的水。
#
# 以序列最外面两条边形成的面基为起始面积，找出两条边中较小的一条，索引加一（i++），
# 原因是找出一条更大的边来代替较小的边，以使得整个容器最大。
# Time: O(n)


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area

if __name__ == "__main__":
    print(Solution().maxArea([3, 4, 5, 1, 3]))