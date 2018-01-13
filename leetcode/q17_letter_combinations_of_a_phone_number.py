# -*- coding: utf-8 -*-  
__author__ = "wangxuan"





class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '' == digits:
            return []

        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }


        from functools import reduce
        # 匿名函数中 acc 表示已经翻译过的数字所组成的字符串集合
        # digit 表示当前正在翻译的数字对应的字母集合
        # 例如：digits "23"
        # 假设2已经翻译过：此时 acc = ['a', 'b', 'c']
        # digit = ['d', 'e', 'f']
        # 匿名函数是一个双重循环，外层遍历acc, 内部遍历digit：
        # x + y 组成新的字符串集合 ['ad', 'ae', 'af', 'bd', 'be', 'bf' ...]
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])


    def letterCombinations2(self, digits):
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0: return []
        return [a + b for a in self.letterCombinations(digits[:-1]) for b in self.letterCombinations(digits[-1])] or list(map[digits])

if __name__ == "__main__":
    print(Solution().letterCombinations2("235"))