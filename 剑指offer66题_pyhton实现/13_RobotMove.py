# -*- coding:utf-8 -*-
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''


class Solution:
    def moving_count(self, threshold, rows, cols):
        if threshold<0 or rows<0 or cols<0:
            return 0
        # 这里用flag_mat = [[True] * cols] * rows会出现地址相同的问题
        flag_mat = [[True for _ in range(cols)] for _ in range(rows)]
        res = self.count_move(threshold, rows, cols, 0, 0, flag_mat)
        return res

    def count_move(self, threshold, rows, cols, i, j, flag_mat):
        '''
        回溯法求解
        '''
        count = 0
        if self.can_in(threshold, rows, cols, i, j, flag_mat):
            flag_mat[i][j] = False
            # 1表示当前节点可以被访问
            count = 1 + self.count_move(threshold, rows, cols, i + 1, j, flag_mat) + \
                        self.count_move(threshold, rows, cols, i - 1, j, flag_mat) + \
                        self.count_move(threshold, rows, cols, i, j + 1, flag_mat) + \
                        self.count_move(threshold, rows, cols, i, j - 1, flag_mat)
        return count


    def can_in(self, threshold, rows, cols, i, j, flag_mat):
        '''
        判断robot能否进入i，j中
        '''
        if 0<=i<rows and 0<=j<cols and flag_mat[i][j] and (self.num_cnt(i)+self.num_cnt(j))<=threshold:
            return True
        return False

    def num_cnt(self, num):
        '''
        计算各个位的和
        '''
        count = 0
        while num>0:
            count += (num%10)
            num = num//10
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.moving_count(5, 10, 10))