'''
矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如在下面的3*4矩阵
a b t g
c f c s
j d e h
矩阵中包含一条字符串”bfce”的路径，但是矩阵中不包含”abfb”路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''


class Solution():
    '''
    这里假设是按照顺序遍历的字符串
    那么第一步是遍历matrix找到第一个元素
    之后递归寻找字符串中下一个元素是否存在
    '''
    def haspath(self, matrix, rows, cols, path):
        '''
        这里先遍历查找第一个是否存在
        若存在，进入find_path函数回溯查找
        '''
        if not matrix or rows<1 or cols<1 or not path:
            return False
        flag_mat = [True]*cols*rows
        for row in range(rows):
            for col in range(cols):
                if matrix[row*cols+col] == path[0]:
                    if self.find_path(matrix, rows, cols, path, flag_mat, row, col, 0):
                        return True
        return False

    def find_path(self, matrix, rows, cols, path, flag_mat, row, col, idx):
        '''
        使用回溯法，当找不到下一个元素时，回到上一个状态
        '''
        if idx == len(path):
            return True
        haspath = False
        if 0<=row<rows and 0<=col<cols and matrix[row*cols+col] == path[idx] and flag_mat[row*cols+col]:
            flag_mat[row * cols + col] = False
            idx += 1
            haspath = self.find_path(matrix, rows, cols, path, flag_mat, row+1, col, idx) or \
                      self.find_path(matrix, rows, cols, path, flag_mat, row-1, col, idx) or \
                      self.find_path(matrix, rows, cols, path, flag_mat, row, col+1, idx) or \
                      self.find_path(matrix, rows, cols, path, flag_mat, row, col-1, idx)
            if not haspath:
                idx -= 1
                flag_mat[row*cols+col] = True
        return haspath


if __name__ == '__main__':
    mat = 'abtgcfcsjdeh'
    sol = Solution()
    # print(sol.haspath(mat, 3, 4, 'bfce'))
    print(sol.haspath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8,"SGGFIECVAASABCEHJIGQEM"))