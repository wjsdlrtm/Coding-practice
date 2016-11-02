# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            l1 = []
        else:
            l1 = l1.val
        if not l2:
            l2 = []
        else:
            l2 = l2.val
        l3 = ListNode(l1 + l2)
        return l3
