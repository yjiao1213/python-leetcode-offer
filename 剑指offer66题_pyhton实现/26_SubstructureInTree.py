# -*- coding:utf-8 -*-
'''
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def HasSubtree(self, pRoot1, pRoot2):
        # 当输入树为空树时，返回False
        if not pRoot1 or not pRoot2:
            return False
        res = False
        # 递归遍历树结构
        if pRoot1.val == pRoot2.val:
            res = self.isSubTree(pRoot1, pRoot2)
        # 当不是子树时，遍历左右节点进行查找
        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def isSubTree(self, pRoot1, pRoot2):
        # 判断root2是否为root1的子树
        if not pRoot2:
            # 当Root2遍历结束时，才返回True
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        # 递归比较左子树的右子树
        return self.isSubTree(pRoot1.left, pRoot2.left) and self.isSubTree(pRoot1.right, pRoot2.right)