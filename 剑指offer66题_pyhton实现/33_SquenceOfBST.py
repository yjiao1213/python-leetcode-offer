# -*- coding:utf-8 -*-
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 二叉搜索树中，根节点的值大于左子树小于右子树
        if not sequence:
            return False
        left, right = [], []
        root = sequence[-1]
        # 判断并提取出left部分
        i = 0
        while i<len(sequence)-1:
            if sequence[i]<root:
                left.append(sequence[i])
            else:
                break
            i += 1
        # 提取right部分
        j = i
        while j < len(sequence)-1:
            if sequence[j]>root:
                right.append(sequence[j])
            else:
                break
            j += 1
        if i < len(sequence)-1 and j < len(sequence)-1:
            # 说明没有遵循一边大于根一边小于根的后序遍历原则
            return False
        # 递归分别求解左右子树
        left_flag = True
        if left:
            left_flag = self.VerifySquenceOfBST(left)
        right_flag = True
        if right:
            right_flag = self.VerifySquenceOfBST(right)
        return left_flag and right_flag


if __name__ == '__main__':
    sol = Solution()
    print(sol.VerifySquenceOfBST([7,4,6,5]))