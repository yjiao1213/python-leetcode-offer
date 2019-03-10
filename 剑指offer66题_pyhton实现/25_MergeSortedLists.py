# -*- coding:utf-8 -*-
'''
合并两个排序链表
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def MergeSortedList(self, head1, head2):
        if not head1 and not head2:
            return None
        if not head1:
            return head2
        if not head2:
            return head1

        if head1.val <= head2.val:
            res = head1
            head1 = head1.next
        else:
            res = head2
            head2 = head2.next
        pnode = res
        while head1 or head2:
            if not head1:
                pnode.next = head2
                break
            if not head2:
                pnode.next = head1
                break
            if head1.val <= head2.val:
                pnode.next = head1
                head1 = head1.next
            else:
                pnode.next = head2
                head2 = head2.next
            pnode = pnode.next
        return res
