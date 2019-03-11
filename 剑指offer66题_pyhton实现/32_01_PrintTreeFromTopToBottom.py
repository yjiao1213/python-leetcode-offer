# -*- coding:utf-8 -*-
'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        list_print = []
        list_print.append(root)
        while list_print:
            node = list_print.pop(0)
            res.append(node.val)
            if node.left:
                list_print.append(node.left)
            if node.right:
                list_print.append(node.right)
        return res