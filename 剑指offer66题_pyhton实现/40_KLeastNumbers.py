# -*- coding:utf-8 -*-
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
'''


class Solution():
    def GetLeastNumbers_Solution(self, tinput, k):
        res = []
        if not tinput or k == 0 or k > len(tinput):
            return res
        start = 0
        end = len(tinput) - 1
        nums, idx = self.partition(tinput, start, end)
        while start <= end:
            if idx > k - 1:
                end = idx - 1
                nums, idx = self.partition(nums, start, end)
            elif idx < k - 1:
                start = idx + 1
                nums, idx = self.partition(nums, start, end)
            else:
                res = nums[:idx + 1]
                break
        return sorted(res)

    def partition(self, nums, start, end):
        idx = end
        small = start
        for i in range(start+1, end):
            if nums[i] < nums[idx]:
                nums[small], nums[i] = nums[i], nums[small]
                small += 1
        if nums[small] < nums[idx]:
            small += 1
        nums[small], nums[idx] = nums[idx], nums[small]
        return nums, small


if __name__ == '__main__':

    s = [4, 5, 1, 6, 2, 7, 3, 8]
    sol = Solution()
    nums= sol.GetLeastNumbers_Solution(s, 1)
    print(nums)