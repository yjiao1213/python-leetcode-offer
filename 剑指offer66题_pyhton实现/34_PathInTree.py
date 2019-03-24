# -*- coding:utf-8 -*-
'''
二叉树中和为某一值的路径
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        res, stack = [], []
        num_sum, node = 0, root
        stack.append(root)
        num_sum += root.val
        while stack:
            while node.left:
                stack.append(node.left)
                node = node.left
                num_sum += node.val
            node = stack[-1]
            if node.right:
                stack.append(node.right)
                node = node.right
                num_sum += node.val
            if not node.right and not node.left:
                # 当到达叶节点时
                if num_sum == expectNumber:
                    # 判断是否为一个答案
                    res.append([item.val for item in stack])
                # 节点删除
                node_del = stack.pop()
                num_sum -= node_del.val
                if stack:
                    node = stack[-1]
                else:
                    break
                # 当删除的节点是上一个节点的右子节点，说明这个节点的左右子节点都被遍历过，需要删除
                while stack and (node.right == node_del or not node.right):
                    node_del = stack.pop()
                    num_sum -= node_del.val
                    if stack:
                        node = stack[-1]
                if stack:
                    node = stack[-1]
                    if node.right:
                        stack.append(node.right)
                        node = node.right
                        num_sum += node.val
        return res

if __name__ == '__main__':
    # {10, 5, 12, 4, 7}, 22
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(12)
    node3 = TreeNode(4)
    node4 = TreeNode(7)
    root.right = node2
    root.left = node1
    node1.right = node4
    node1.left = node3

    sol = Solution()
    print(sol.FindPath(root, 22))