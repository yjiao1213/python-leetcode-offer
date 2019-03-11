# -*- coding:utf-8 -*-
'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def Print(self, pRoot):
        res = []
        if not pRoot:
            return res
        layer = []
        num_now = 1
        layer.append(pRoot)
        while layer:
            res1 = []
            num_next = 0
            while num_now:
                num_now -= 1
                node = layer.pop(0)
                res1.append(node.val)
                if node.left:
                    layer.append(node.left)
                    num_next += 1
                if node.right:
                    layer.append(node.right)
                    num_next += 1
            num_now = num_next
            res.append(res1)
        return  res