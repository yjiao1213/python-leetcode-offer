# -*- coding:utf-8 -*-
'''
连续子数组最大和
'''
class Solution():
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        sum1 = array[0]
        res = array[0]
        for i in range(1, len(array)):
            if sum1 + array[i] > array[i]:
                sum1 = sum1 + array[i]
            else:
                sum1 = array[i]
            res = max(sum1, res)
        return res