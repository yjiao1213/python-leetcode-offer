# -*- coding:utf-8 -*-
'''
题目：输入一个链表，输出该链表中倒数第k个结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def KthFromEnd(self, head, k):
        p1 = head
        p2 = head
        if not head or k<=0:
            return None

        i = 0
        while p2.next != None:
            if i >= k-1:
                p1 = p1.next
            p2 = p2.next
            i += 1
        return p1


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    # 1->2->3
    sol = Solution()
    print(sol.KthFromEnd(node1,3).val)