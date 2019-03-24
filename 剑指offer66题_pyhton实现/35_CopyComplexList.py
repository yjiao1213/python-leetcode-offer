# -*- coding:utf-8 -*-
'''
复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用）
'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# 使用哈希表的方法 时间复杂度O(n) 空间复杂度O(n)
class Solution_1():
    def Clone(self, pHead):
        if not pHead:
            return None
        dic = {None:None}
        pnode = pHead
        # 建立头节点
        head = RandomListNode(pnode.label)
        node = head
        dic[pnode] = node
        pnode = pnode.next
        # 按照next顺序，复制链表
        while pnode:
            node.next = RandomListNode(pnode.label)
            node = node.next
            dic[pnode] = node
            pnode = pnode.next
        # 给random赋值
        node, pnode = head, pHead
        while pnode:
            node.random = dic[pnode.random]
            node = node.next
            pnode = pnode.next
        return head

# 使用在原节点后添加新节点的方法 时间复杂度O(n) 空间复杂度O(1)
class Solution_2():

    def Clone(self, pHead):
        if not pHead:
            return None
        self.pnode = pHead
        self.CloneNodes()
        self.pnode = pHead
        self.CloneRandom()
        self.pnode = pHead
        return self.Clonesplit()

    def CloneNodes(self):
        # 把新建节点放到旧节点的后面
        while self.pnode:
            node = RandomListNode(self.pnode.label)
            _node = self.pnode.next
            self.pnode.next = node
            node.next = _node
            self.pnode = _node

    def CloneRandom(self):
        # 定义
        while self.pnode:
            node = self.pnode.next
            if self.pnode.random:
                node.random = self.pnode.random.next
            self.pnode = self.pnode.next.next

    def Clonesplit(self):
        if self.pnode:
            head = self.pnode.next
            node = head
            self.pnode.next = node.next
            self.pnode = self.pnode.next
        while self.pnode:
            node.next = self.pnode.next
            node = node.next
            self.pnode.next = node.next
            self.pnode = self.pnode.next
        return head

if __name__ == '__main__':
    phead = RandomListNode(0)
    node1 = RandomListNode(1)
    phead.next = node1
    phead.random = node1
    sol = Solution_2()
    print(sol.Clone(phead).label)