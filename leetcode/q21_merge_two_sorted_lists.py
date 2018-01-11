# -*- coding: utf-8 -*-  
__author__ = "wangxuan"

# Merge two sorted linked lists and return it as a new list
# The new list should be made by splicing together the nodes of the first two lists
#
# Example:
# input: 1->2->4, 1->3->4
# output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # 相当于java中的toString()
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0) # 初始化一个LinkedList
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next

    def mergeTwoLists2(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l2.next, l1)
            return l2

if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode(2)
    l2.next = ListNode(3)

    print(Solution().mergeTwoLists2(l1, l2))


