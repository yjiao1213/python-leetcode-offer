# -*- coding:utf-8 -*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        使用字典
        """
        dic = {}
        for i, num in enumerate(nums):
            if target-num in dic.keys():
                return dic[target-num], i
            dic[num] = i
        return None 