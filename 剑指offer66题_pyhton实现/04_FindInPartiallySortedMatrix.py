'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

# 时间复杂度O(n)
class Solution():
    '''
    解决方法是从矩阵右上角的数字m开始寻找，坐标为 i = 0, j = n
    分三种情况：
        若相等，输出结果
        若m>target，那么j--
        若m<target,那么i++
    注意边界判断
    这里输入的数组中的元素只能是数字，如果数组中有其他类型变量则会报错
    '''
    def find_in_mat(self, input_mat, target):
        if not input_mat:
            return False
        res = False
        max_i = len(input_mat)
        i = 0
        j = len(input_mat[0])-1
        while j>=0 and i<max_i:
            m = input_mat[i][j]
            if m == target:
                res = True
                break
            elif target > m:
                i = i+1
            else:
                j = j-1
        return res


if __name__ == '__main__':
    mat1 = []
    mat2 = [[1, 2, 8, 9],
            [2, 4, 9, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15]]
    mat3 = [[62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
            [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
            [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82],
            [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
            [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
            [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]]

    sol = Solution()
    print(sol.find_in_mat(mat1, 0))
    print(sol.find_in_mat(mat2, 8))
    print(sol.find_in_mat(mat2, 3))
    print(sol.find_in_mat(mat2, 16))
    print(sol.find_in_mat(mat2, 0))
    print(sol.find_in_mat(mat3, 61))
    print(sol.find_in_mat(mat3, 86))
    print(sol.find_in_mat(mat3, 75))