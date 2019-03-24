# -*- coding:utf-8 -*-
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0
'''
class Solution():
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dic_num = {}
        for num in numbers:
            if num in dic_num.keys():
                dic_num[num] += 1
            else:
                dic_num[num] = 1
        for k,v in dic_num.items():
            if v > int(len(numbers)/2):
                return k
        return 0