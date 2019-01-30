'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# O(n^2)的时间复杂度是不合格的

class Solution():
    '''
    问题有两种，一类是在原数组中修改，一种是可以新建数组作为结果
    '''
    def Replace_in_place(self, str):
        '''
        在原数组中进行修改，使用书中给的思路
        双指针法，时间复杂度为O(n)
        '''
        num_space = 0
        for item in str:
            if item == ' ':
                num_space += 1
        # 由于python中字符串是不能被修改的，所以需要这里用list代替
        new_str = list(str) + [None]*num_space*2
        idx_org, idx_new = len(str)-1, len(str) + num_space*2 -1
        while idx_org != idx_new:
            if new_str[idx_org] == " ":
                new_str[idx_new] = "0"
                new_str[idx_new-1] = "2"
                new_str[idx_new-2] = "%"
                idx_new -= 3
            else:
                new_str[idx_new] = str[idx_org]
                idx_new -= 1
            idx_org -= 1
        return "".join(new_str)

    def Replace_new_place(self, str):
        '''
        使用python的话会有许多种O(n)的解法
        这里使用字符串拼接的方法，形成新字符串
        '''
        res = ""
        space = "%20"
        for item in str:
            if item == " ":
                res = res + space
            else:
                res = res + item
        return res


if __name__ == '__main__':
    str1 = " "
    str2 = 'We Are Happy. '

    sol = Solution()
    print(sol.Replace_in_place(str1))
    print(sol.Replace_new_place(str1))
