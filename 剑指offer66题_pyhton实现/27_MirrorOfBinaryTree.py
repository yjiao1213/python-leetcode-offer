# -*- coding:utf-8 -*-
'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sol = Solution()
    res = sol.Mirror(root)
    print(res.left.val)