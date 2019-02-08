'''
输入一个整数，输出该数二进制表示中1的个数。
'''

# 学习了一下python如何处理二进制数字
class Solution():
    def NumberOf1InBinary(self, n):
        # 注意负数平移问题，负数会形成死循环，因此需要转化
        count = 0
        if n<0:
            n = n & 0xffffffff
        while n:
            # 判断二进制最后一位是否为1，也就是判断是否为奇数
            # 之后向右移位，继续判断
            if n&1 == 1:
                count += 1
            n = n>>1
        return count

    def NumberOf1InBinary01(self, n):
        # 使用bin()函数把十进制转换为字符串格式的二进制
        if n<0:
            str_n = bin(n & 0xffffffff)
        else:
            str_n = bin(n)
        return str_n.count("1")

    def NumberOf1(self, n):
        '''
        书上的方法
        把原数减一时，其实是把最右边的1置为0，那么再与原数做与操作
        循环直到原数为零
        '''
        count = 0
        if n<0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n-1)&n
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.NumberOf1(-1))
    print(sol.NumberOf1(9))