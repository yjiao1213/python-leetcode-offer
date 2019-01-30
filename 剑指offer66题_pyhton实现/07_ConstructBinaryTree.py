'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


# 首先定义树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    '''
    前序遍历的第一个元素为根节点，在中序遍历中，相同的数字，左边为左子树，右边为右子树
    递归法建立树
    '''
    def cons_Btree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        l_inorder, r_inorder = inorder[:inorder.index(preorder[0])], inorder[inorder.index(preorder[0])+1:]
        l_preorder, r_preorder = preorder[1:1+len(l_inorder)], preorder[1+len(l_inorder):]
        root.left = self.cons_Btree(l_preorder, l_inorder)
        root.right = self.cons_Btree(r_preorder, r_inorder)
        return root


if __name__ == '__main__':
    porder = [1,2,4,7,3,5,6,8]
    iorder = [4,7,2,1,5,3,8,6]

    sol = Solution()
    root = sol.cons_Btree(porder, iorder)
