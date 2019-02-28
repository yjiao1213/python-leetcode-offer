# -*- coding:utf-8 -*-
'''
打印1到最大的n位数
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''

class Soltuion(object):
    '''
    用字符串模拟数字加法
    需要考虑大数问题
    '''
    def Print1toMax(self, n):
        # 建立n长的数组
        num = ['0']*n

        while not self.Increment(num):
            self.Printnum(num)

    def Increment(self, num):
        # 判断是否已经加满
        isOverFlow = False
        # 进位标志
        nTakeOver = 0
        for i in range(len(num)-1, -1, -1):  # 从个位开始计算进位
            nSum = int(num[i]) + nTakeOver   # 计算当前位

            if i == len(num)-1:
                nSum += 1 # 完成对num+1的操作

            if nSum >= 10:  # 进位时
                if i == 0:
                    # 说明已经满了
                    isOverFlow = True
                else:
                    nTakeOver = 1
                    nSum = nSum - 10
                    num[i] = str(nSum)
            else:
                num[i] = str(nSum)
                break
        return isOverFlow

    def Printnum(self, num):
        firstnot0 = False
        for i in range(len(num)):
            if num[i] != '0' or firstnot0:
                firstnot0 = True
                print('%c' % num[i], end='')
        print(' ')



if __name__ == '__main__':
    s = Soltuion()
    s.Print1toMax(n=3)
