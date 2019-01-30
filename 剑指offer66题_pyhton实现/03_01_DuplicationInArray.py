'''
找出数组中重复的数字
在一个长度为n的数组里所有数字都在0~n-1的范围内，数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道重复了多少次
找出任意一个重复的数字
'''


# 使用哈希表解决
# 时间复杂度O(n),空间复杂度O(n)
class Solution1():
    def solve(self, list1):
        dic = dict()
        res = -1
        for item in list1:
            if item in dic.keys():
                res = item
                break
            else:
                dic[item] = 1
        return res


# 换位法，利用所有数字都在0~n-1的范围内的特点
# 时间复杂度O(n),空间复杂度O(1)
class Solution2():
    def solve(self, list1):
        res = -1
        for i in range(len(list1)):
            if list1[i] == i:
                continue
            else:
                if list1[i] == list1[list1[i]]:
                    res = list1[i]
                    break
                else:
                    m = list1[list1[i]]
                    list1[list1[i]], list1[i] = list1[i], m
        return res


if __name__ == '__main__':
    # 测试集合
    list1 = [2,3,1,0,2,5,3]
    list2 = []
    list3 = [1,2,3,4,0,5]

    # sol1 = Solution1()
    # print(sol1.solve(list3))

    # sol2 = Solution2()
    # print(sol2.solve(list1))