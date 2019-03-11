# -*- coding:utf-8 -*-
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的
字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"
和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


class Solution(object):
    def Match(self, s, pattern):
        # 进入递归过程
        return self.matchCore(s, pattern)

    def matchCore(self, s, p):
        if len(p) == 0 and s:
            # 当s不为空，pattern为空时，返回False
            return False
        if not s and not p:
            # 只有当两个数列都减少到长度0，说明匹配成功
            return True
        if len(p) >= 2 and p[1] == '*':
            # 当p中第二个是'*'时
            if len(s)>=1 and (p[0] == s[0] or p[0] == '.'):
                # '*'前面的字符能够匹配s时，后续分三种情况，这三种情况只要有一种情况符合条件就为True
                # 1.'*'匹配了一次  2.'*'匹配了多0次 3. '*'匹配了多次
                return self.matchCore(s[1:], p[2:]) or self.matchCore(s, p[2:]) or self.matchCore(s[1:], p)
            else:
                # '*'前面的字符不能够匹配s时，'*'匹配了0次
                return self.matchCore(s, p[2:])

        if len(s)>=1 and (p[0] == s[0] or p[0] == '.'):
            # 不带'*'的匹配
            return self.matchCore(s[1:], p[1:])
        # 其余情况均为False
        return False


if __name__ == '__main__':
    a = 'aaa'
    p = 'aaaa*'
    sol = Solution()
    print(sol.Match(a,p))