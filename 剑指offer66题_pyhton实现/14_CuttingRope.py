# -*- coding:utf-8 -*-
'''
剪绳子：
给定一根长度为n的绳子，请把绳子剪为m段（m>1, n>1）
每段绳子长度为k[0],k[1]...,k[m]
问所有绳子最大的乘积为多少？
'''


class Solution:
    def cut_DP_up_down(self, n):
        '''
        自顶向下的动态规划
        有大量重复的计算
        '''
        if n < 4:
            return self.check_n(n)
        max_num = 1
        for i in range(1, n):
            num = max(self.cut_DP_up_down(i), i)*max(self.cut_DP_up_down(n-i), n-i)
            max_num = max(num, max_num)
        return max_num
    def cut_DP_down_top(self, n):
        '''
        自下向上的动态规划
        避免了重复计算
        '''
        if n < 4:
            return self.check_n(n)
        f = [0 for _ in range(n+1)]
        f[0] = 0
        f[1] = 1
        f[2] = 2
        f[3] = 3
        if n > 3:
            for i in range(4, n+1):
                max_num = 1
                for j in range(i):
                    max_num = max(max_num, f[j]*f[i-j])
                f[i] = max_num
        return f[n]
    def cut_GA(self, n):
        '''
        用greedy algorithm计算
        当大于等于五时，每当长度为3时分割一次
        当n>=5时，2(n-2)>n，3(n-3)>n,因此意味着当分为3和2时，乘积的大小要大于不分割时候的值
        2(n-2)<3(n-3), 因此应该长度为3时剪一次
        '''
        if n <= 4:
            return self.check_n(n)

        three_num = n // 3
        rem = n % 3
        return rem * (3 ** three_num)
    def check_n(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4



if __name__ == "__main__":
    sol = Solution()
    print(sol.cut_DP_up_down(8))
    print(sol.cut_DP_down_top(8))
    print(sol.cut_GA(8))