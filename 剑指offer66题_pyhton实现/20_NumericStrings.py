# -*- coding:utf-8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"
和"12e+4.3"都不是。
'''


class Solution(object):
    def isNum(self, s):
        # [+-][A][.][B][e,E][+-][C]
        if not s:
            return False
        # 扫描符号部分
        if s[0] == '+' or s[0] =='-':
            s = s[1:]
        if not s:
            return False
        # 扫描A部分
        while s:
            if '0'<=s[0]<='9':
                s = s[1:]
            elif s[0] in ['E', 'e', '.']:
                break
            else:
                return False
        if not s:
            return True
        # 小数点
        if s[0] == '.':
            s = s[1:]
            # B部分
            while s:
                if '0' <= s[0] <= '9':
                    s = s[1:]
                elif s[0] in ['E', 'e']:
                    break
                else:
                    return False
        if not s:
            return True
        # e，E部分
        if s[0] in ['E', 'e']:
            # 符号部分
            s = s[1:]
            if not s:
                return False
            if s[0] == '+' or '-':
                s = s[1:]
            # C部分
            while s:
                if '0' <= s[0] <= '9':
                    s = s[1:]
                elif s[0] in ['E', 'e']:
                    break
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isNum('12e-1'))

