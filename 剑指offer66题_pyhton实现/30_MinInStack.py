# -*- coding:utf-8 -*-
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''
class Solution():
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        self.stack.append(node)
        if not self.minstack:
            self.minstack.append(node)
        else:
            self.minstack.append(min(node, self.minstack[-1]))

    def pop(self):
        if not self.stack:
            return None
        self.minstack.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def min(self):
        if not self.stack:
            return None
        return self.minstack[-1]
