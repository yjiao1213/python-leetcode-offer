'''
输入一个链表，从尾到头打印链表每个节点的值。
'''


# 单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    '''
    先顺序遍历，储存在栈中
    从栈中输出
    O(n)
    '''
    def reverse_order(self, head):
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        while stack:
            print(stack.pop())


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    singleNode = ListNode(12)

    sol = Solution()
    # sol.reverse_order(node1)
    sol.reverse_order(singleNode)