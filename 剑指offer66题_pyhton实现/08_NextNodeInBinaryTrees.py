'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''


# 首先定义树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution():
    '''
    要求的是中序遍历中的下一个节点，可以分为三种情况
    1. 当前节点存在右子节点，那么下一个节点就是当前节点的右子树的最左子节点（左））
    2. 当前节点无右子结点，那么下一个节点就是当前节点的父子节点 （左→根
    3. 当前节点无右子节点，并且是父节点的右子节点，那么需要一直查找查找父节点是否是父节点的父节点的左子节点，
       如果存在那么下一个节点就是父节点的父节点 （右→左→→根）
    '''
    def find_next_node(self, cur_node):
        next_node = None
        if cur_node.right:
            head = cur_node.right
            while head:
                next_node = head
                head = head.left
        elif cur_node.parent:
            p_node = cur_node.parent
            if p_node.right == cur_node:
                child = cur_node
                while p_node.left != child and p_node:
                    child = p_node
                    p_node = p_node.parent
                next_node = p_node
            else:
                next_node = p_node
        return next_node


if __name__ == '__main__':
    # 建立树
    # 不知道如何批量生成类变量，所以就用这种方法了
    a, b, c, d = TreeNode('a'), TreeNode('b'), TreeNode('c'), TreeNode('d')
    e, f, g, h, i = TreeNode('e'), TreeNode('f'), TreeNode('g'), TreeNode('h'), TreeNode('i')
    a.left, a.right = b, c
    b.left, b.right, b.parent = d, e, a
    e.left, e.right, e.parent = h, i, b
    c.left, c.right, c.parent = f, g, a
    d.parent, h.parent, i.parent, f.parent, g.parent = b, e, e, c, c
    sol = Solution()
    print(sol.find_next_node(a).val) # case 1
    # print(sol.find_next_node(f).val)  # case 2
    # print(sol.find_next_node(i).val)  # case 3