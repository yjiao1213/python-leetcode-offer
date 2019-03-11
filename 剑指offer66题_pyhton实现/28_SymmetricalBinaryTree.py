# -*- coding:utf-8 -*-
'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution():
    def isSymmetrical(self, pRoot):
        return self.isSyCore(pRoot, pRoot)

    def isSyCore(self, pleft, pright):
        if not pleft and not pright:
            return True
        if not pleft or not pright:
            return False
        if pleft.val == pright.val:
            return self.isSyCore(pleft.left, pright.right) and self.isSyCore(pleft.right, pright.left)
        else:
            return False
