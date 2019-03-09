# -*- coding:utf-8 -*-
'''
输入一个链表，反转链表后，输出链表的所有元素。
三指针法
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def ReverseList(self, head):
        if not head:
            return None
        if head.next == None:
            return head
        if head.next.next == None:
            node2 = head
            node3 = head.next
        else:
            node1 = head
            node2 = head.next
            node3 = head.next.next
            node1.next = None
            while True:
                # node1 < node2 > node3
                node2.next = node1
                if node3.next == None:
                    break
                # 保持node1 > node2 > node3的顺序
                node1 = node2
                node2 = node3
                node3 = node3.next
        node3.next = node2
        return node3