# -*- coding:utf-8 -*-
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1   2   3   4
                              5   6   7   8
                              9  10  11  12
                             13  14  15  16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
class Solution():
    def printMatrix(self, matrix):
        res = []
        # 数组为空时
        if not matrix:
            return []
        # 只有一行或者一列
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                res.append(matrix[i][0])
            return res
        # 第一行
        for i in range(len(matrix[0])):
            res.append(matrix[0][i])
        # 最后一列
        for i in range(1, len(matrix)):
            res.append(matrix[i][-1])
        # 最后一行（倒序）
        if len(matrix) > 1:
            for i in range(len(matrix[0])-2, -1, -1):
                res.append(matrix[-1][i])
        # 第一列（倒叙）
        if len(matrix[0]) > 1:
            for i in range(len(matrix)-2, 0, -1):
                res.append(matrix[i][0])

        # 当矩阵大于等于2乘2时，传递
        if len(matrix)>2 and len(matrix[0])>2:
            res.extend(self.printMatrix([matrix[i][1:-1] for i in range(1, len(matrix)-1)]))
        return res


if __name__ == "__main__":
    list1 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10,11,12],
             [13,14,15,16]]
    sol = Solution()
    print(sol.printMatrix([[1],[2],[3],[4],[5]]))