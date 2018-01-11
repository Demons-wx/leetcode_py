# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# 给定两个非空链表，表示两个非负整数。数字以相反的顺序存储，每个节点包含一个数字，
# 将这两个数字相加并作为链表返回。
#
# Example:
# Input: (2->4->3) + (5->6->4)
# Output: 7->0->8
# Explanation: 342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next

        num1, num2 = 0, 0
        while stk1:
            num1 *= 10
            num1 += stk1.pop()

        while stk2:
            num2 *= 10
            num2 += stk2.pop()

        total = num1 + num2

        prev, head = None, None
        for i in str(total):
            head = ListNode(i)
            head.next = prev
            prev = head

        return head



if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(l1, l2))