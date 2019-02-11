'''
数值的整数次方：
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
不使用库函数，不考虑大数问题
'''


class Solution():
    def Power(self, base, exponent):
        '''
        可以适用递归减少运算，当计算的当前的exponent时，只需要计算exponent/2时的值就可以
        比如计算base的8次方时，只需要计算出4次方就可以，当计算base的9次方时，只需要计算4次方相乘再乘base就可以
        这里使用向右移位的方法来代替除以2的操作
        注意指数为负数，指数为0和base为0的问题
        '''
        if base == 0:
            return 0
        if exponent == 0:
            return 1

        if exponent == -1:
            return 1/base
        if exponent == 1:
            return base
        res = self.Power(base, exponent>>1)
        res *= res
        if exponent & 0x1 == 1:
            res *= base

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.Power(5, 3))