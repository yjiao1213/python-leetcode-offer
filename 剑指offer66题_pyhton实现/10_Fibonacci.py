'''
求斐波那契数列的第n项
'''


class Solution1:
    '''
    效率低的递归法，重复计算太多
    不推荐，时间复杂为指数级
    '''
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


class Solution2:
    '''
    避免重复计算的递归
    可用查表法和自下而上的循环
    这里采用书中的方法，使用自下而上的循环
    还有一种利用公式的解法，这里就不给出了
    '''
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib1, fib2 = 0, 1
            res = 0
            for i in range(n-1):
                res = fib1 + fib2
                fib1 = fib2
                fib2 = res
            return res

    def simply_sol(self, n):
        '''
        在网上看到一个简洁的方法，复制在这里，学习一下
        '''
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                tempArray[i % 2] = tempArray[0] + tempArray[1]
        return tempArray[n % 2]


if __name__ == "__main__":
    sol1 = Solution1()
    for i in range(8):
        print(sol1.fibonacci(i))
    sol2 = Solution2()
    for i in range(8):
        print(sol2.fibonacci(i))