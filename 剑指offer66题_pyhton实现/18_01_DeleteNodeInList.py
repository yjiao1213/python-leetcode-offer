# coding=utf-8
"""
O(1)时间删除链表结点
如果有后续结点，后续结点的值前移，删除后续结点，如果没有，只能顺序查找了
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def del_node(self, head, node):
        '''
        分三种情况，1. 删除的节点为头节点
                    2. 删除的节点是尾节点
                    3. 其他
        :param head: 链表头
        :param node: 要删除的节点
        '''
        if head == node:
            del node
        elif node.next == None:
            pnode = head
            while pnode.next != node:
                pnode = pnode.next
            pnode.next = None
            del node
        else:
            node.val = node.next.val
            n_node = node.next
            node.next = node.next.next
            del n_node


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node1.next.next = node3
    sol = Solution()
    sol.del_node(node1, node2)
    print(node1.val, node1.next.val)