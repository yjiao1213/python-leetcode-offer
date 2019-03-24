# -*- coding:utf-8 -*-
'''
二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        # 记录链表头和链表已排序位置
        self.head = None
        self.tail = None

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        if not self.head and not self.tail:
            self.head = pRootOfTree
            self.tail = pRootOfTree
        else:
            self.tail.right = pRootOfTree
            pRootOfTree.left = self.tail
            self.tail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.head