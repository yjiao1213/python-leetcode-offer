# -*- coding:utf-8 -*-
'''
序列化和反序列化二叉树
直接用前序遍历
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        self.s = []
        self.SerializeCore(root)
        return self.s

    def SerializeCore(self, root):
        if not root:
            self.s.append('*')
        else:
            self.s.append(str(root.val))
            self.SerializeCore(root.left)
            self.SerializeCore(root.right)

    def Deserialize(self, s):
        # write code here
        self.s_read = s
        pHead = self.DeserializeCore()
        return pHead

    def DeserializeCore(self):
        if not self.s_read:
            return None
        a = self.s_read.pop(0)
        if a == '*':
            return None
        else:
            pHead = TreeNode(int(a))
            pHead.left = self.DeserializeCore()
            pHead.right = self.DeserializeCore()
        return pHead