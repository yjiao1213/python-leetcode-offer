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
    
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target-nums[i])+i+1]
        return []
        
