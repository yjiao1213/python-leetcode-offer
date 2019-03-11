# -*- coding:utf-8 -*-
'''
请实现一个函数按照之字形打印二叉树
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
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
        layer_now, layer_next, lay = [], [], 0
        layer_now.append(pRoot)
        while layer_now:
            res1 = []
            while layer_now:
                node = layer_now.pop()
                res1.append(node.val)
                if lay%2 == 0:
                    if node.left:
                        layer_next.append(node.left)
                    if node.right:
                        layer_next.append(node.right)
                if lay%2 == 1:
                    if node.right:
                        layer_next.append(node.right)
                    if node.left:
                        layer_next.append(node.left)
            lay += 1
            layer_now = layer_next
            layer_next = []
            res.append(res1)
        return res
        # layer = []
        # lay = 1
        # layer.append(pRoot)
        # layer_now = 1
        # while layer:
        #     res1 = []
        #     layer_next = 0
        #     while layer_now:
        #         layer_now -= 1
        #         node = layer.pop(0)
        #         res1.append(node.val)
        #         if lay%2 == 0:
        #             if node.left:
        #                 layer.append(node.left)
        #                 layer_next += 1
        #             if node.right:
        #                 layer.append(node.right)
        #                 layer_next += 1
        #         if lay%2 == 1:
        #             if node.right:
        #                 layer.append(node.right)
        #                 layer_next += 1
        #             if node.left:
        #                 layer.append(node.left)
        #                 layer_next += 1
        #     lay += 1
        #     res.append(res1)
        #     layer_now = layer_next
        # return res