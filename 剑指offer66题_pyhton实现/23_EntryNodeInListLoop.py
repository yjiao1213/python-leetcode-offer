# -*- coding:utf-8 -*-
'''
一个链表中包含环，请找出该链表的环的入口结点。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def ListLoop(self, head):
        if not head.next or not head.next.next:
            return None
        walk = head.next
        run = head.next.next
        while walk != run:
            if not run.next or not run.next.next:
                return None
            walk = walk.next
            run = run.next.next
        meet_node = run
        walk_1 = head
        walk_2 = meet_node
        while walk_1 != walk_2:
            walk_1 = walk_1.next
            walk_2 = walk_2.next
        return walk_1