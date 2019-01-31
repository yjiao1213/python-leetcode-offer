'''
用两个栈实现一个队列，并完成在尾部插入节点和在头部删除节点两个功能（也就是队列的pop和push操作）
'''


class Queuewithstacks():
    '''
    栈1用来输入，栈2用来输出
    输入时直接把数据push入栈1中
    输出是如果栈2为空，把栈1全部元素元素pop出并push到栈2中，pop栈2
          如果栈2不为空，直接pop栈2
    '''
    def __init__(self):
        self.stack1_in = []
        self.stack2_out = []

    def push(self, x):
        self.stack1_in.append(x)

    def pop(self):
        if not self.stack1_in and not self.stack2_out:
            return None
        elif self.stack2_out:
            return self.stack2_out.pop()
        else:
            while self.stack1_in:
                self.stack2_out.append(self.stack1_in.pop())
            return self.stack2_out.pop()


if __name__ == '__main__':
    P = Queuewithstacks()
    P.push(10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())