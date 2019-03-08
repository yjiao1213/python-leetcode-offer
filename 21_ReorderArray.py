# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分
'''

class Solution(object):
    def ReorderArray(self, input):
        if len(input) < 2:
            return input
        i = 0
        j = len(input)-1
        while i<j:
            while input[i]%2==1 and i<j:
                i = i+1
            while input[j]%2==0 and j>i:
                j = j-1
            input[i], input[j] = input[j], input[i]
            i = i+1
            j = j-1
        # return input

if __name__ == '__main__':
    a = [2,1]
    sol = Solution()
    sol.ReorderArray(a)
    print(a)