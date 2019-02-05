'''
旋转数组的最小数字:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


class Solution():
    '''
    利用数组的排序关系，可以用二分查找
    时间复杂度为O(logn)
    使用两个指针left和right分别指向数组的第一个和最后一个元素
    再用一个指针mid指向他们之间的元素
    当mid>=left时，最小元素应该在mid的右边
    当mid<=right时，最小元素应该在mid的左边
    当left和right相邻时，就可以找到最小的元素为right
    hint: 要考虑三种特殊情况 1. 序列为递增序列 2. 当left，right和mid都相同时
    '''
    def find_min(self, input):
        res = 0
        if input:
            left, right = 0, len(input)-1
            mid = (left + right) // 2
            if input[left] > input[right]:
                while right-left > 1:
                    mid = (left + right) // 2
                    if input[mid] >= input[left]:
                        left = mid
                    elif input[mid] <= input[right]:
                        right = mid
                res = input[right]
            elif input[left] < input[right]:
                # 序列为递增序列时，输出第一个元素
                res = input[left]
            elif input[left] == input[right] == input[mid]:
                # 当无法判断时，遍历寻找最小.O(n)
                res = min(input)

        return res


if __name__ == '__main__':
    check1 = [3,4,5,1,2]
    check2 = [1,2,3,4,5]
    check3 = [1,1,1,0,1]
    check4 = [1,0,1,1,1]
    check5 = []
    check6 = [1]
    sol = Solution()
    print(sol.find_min(check6))